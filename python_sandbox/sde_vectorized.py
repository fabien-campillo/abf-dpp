import numpy as np


def sde_vectorized(f, g, X0, T, N, R):
    """
    Vectorized simulation of an SDE using the Euler-Maruyama scheme.

    Parameters:
        f: Function f(t, X) -> ndarray, drift term of SDE.
        g: Function g(t, X) -> ndarray of shape (n, d), diffusion term of SDE.
        X0: Initial condition, ndarray of shape (n,).
        T: Final time.
        N: Number of time steps (N+1: number of time instants)
        R: Number of independent realizations.

    Understand:
        n state space dimension given by n = len(X0)         i=1:n
        d noise dimension (implicitly defined ????)          j=1:d
        r realization index                                  r=1:R
        k time index, t_k = k * dt = i * T/N for k=0:N
        i dimension index, i=1:n

    Returns:
        t_vals: Array of time points.
        X_vals: Array of shape (R, N+1, n), simulated paths of X_t.
    """
    # --------------------------------------------------------------------------------
    # --- some tests about dimension coherence ---------------------------------------
    # --------------------------------------------------------------------------------

    # X0 will be of dimension (n,R)
    # n the dimension of the diffusion process and R
    # the number of independent realizations

    # Ensure X0 is a 2D array
    if not isinstance(X0, np.ndarray) or X0.ndim != 2:
        raise ValueError("X0 must be a 2D NumPy array of shape (n, R).")

    n, R = X0.shape  # Deduce n and R from X0

    # Dimensions
    n = len(X0)  # Dimension of X
    dt = T / N  # Time step size
    t_vals = np.linspace(0, T, N + 1)  # Time points

    # Pre-allocate array for results
    X_vals = np.zeros((R, N + 1, n))
    # Initialize paths
    X_vals[:, 0, :] = X0  # Set initial condition for all realizations

    # Check the dimensions of f and g before starting the simulation
    # Check the dimensions of f
    f_result = f(t[0], X[:, :, 0])  # Evaluate f at the first time step
    if f_result.shape != (n, R):
        raise ValueError(f"Function f(t, X) should return an array of shape (n, R), but got {f_result.shape}.")

    # Check the dimensions of g
    g_result = g(t[0], X[:, :, 0])  # Evaluate g at the first time step
    if g_result.shape != (n, d, R):  # Assuming d is the number of noise dimensions
        raise ValueError(f"Function g(t, X) should return an array of shape (n, d, R), but got {g_result.shape}.")

    # Generate Brownian increments for all realizations
    dW = np.random.normal(0, np.sqrt(dt), size=(R, N, n))  # Shape (R, N, n)

    # Vectorized iteration
    for i in range(N):
        current_t = t_vals[i]
        current_X = X_vals[:, i, :]  # Current state for all realizations
        drift = f(current_t, current_X)  # Shape (R, n)
        # Einstein summation convention :
        #    summation along j-index
        #    to get a Shape (R, n) from (R, d, n)*(R, n)
        diffusion = np.einsum("rji,rj->ri", g(current_t, current_X), dW[:, i, :])  # Shape (R, n)
        X_vals[:, i + 1, :] = current_X + drift * dt + diffusion  # Update for all realizations

    return t_vals, X_vals
