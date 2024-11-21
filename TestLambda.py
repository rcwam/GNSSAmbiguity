import georinex as gr
import numpy as np

def lambda_method(Q, a):
    """
    LAMBDA method for integer least-squares estimation.
    
    Parameters:
    Q (numpy.ndarray): Covariance matrix of the float ambiguities.
    a (numpy.ndarray): Vector of float ambiguities.
    
    Returns:
    numpy.ndarray: Vector of integer ambiguities.
    """
    L = np.linalg.cholesky(Q)
    
    # Ensure a is a column vector
    if a.ndim == 1:
        a = a[:, np.newaxis]
    
    Z = np.linalg.inv(L).dot(a)
    a_int = np.round(Z)
    a_hat = L.dot(a_int)
    
    return a_hat

# Load RINEX file
rinex_file = r'C:\Swadesh\Work\Research Topics\Quantum\Lambda\data\APO100USA_R_20241371500_01H_30S_MO.crx'  # Replace with your RINEX file path
data = gr.load(rinex_file)

# Extract carrier-phase observations
L1C = data['L1C'].values.flatten()  # Ensure it's a 1D array
L2W = data['L2W'].values.flatten()  # Ensure it's a 1D array

# Ensure the observations have the same length
if L1C.shape[0] != L2W.shape[0]:
    raise ValueError("L1C and L2W must have the same length")

# Compute float ambiguities (simplified example)
def compute_float_ambiguities(L1C, L2W):
    float_ambiguities = L1C - L2W  # Simplified example
    return float_ambiguities

float_ambiguities = compute_float_ambiguities(L1C, L2W)

# Ensure float_ambiguities is a column vector
if float_ambiguities.ndim == 1:
    float_ambiguities = float_ambiguities[:, np.newaxis]

# Estimate covariance matrix (simplified example)
def estimate_covariance_matrix(L1C, L2W):
    stacked = np.vstack((L1C, L2W))
    Q = np.cov(stacked)  # Ensure correct shape
    return Q

Q = estimate_covariance_matrix(L1C, L2W)

# Ensure Q is square and matches the length of float_ambiguities
if Q.shape[0] != Q.shape[1] or Q.shape[0] != float_ambiguities.shape[0]:
    raise ValueError("Covariance matrix Q must be square and match the length of float ambiguities")

# Apply LAMBDA method
a = float_ambiguities
a_hat = lambda_method(Q, a)
print("Estimated integer ambiguities:", a_hat)