#Example Covariance and float ambiguities
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
    # Decorrelate the ambiguities
    L = np.linalg.cholesky(Q)
    Z = np.linalg.inv(L).dot(a)
    
    # Round to nearest integer
    a_int = np.round(Z)
    
    # Transform back to original space
    a_hat = L.dot(a_int)
    
    return a_hat

# Read RINEX file
rinex_file = r'C:\Swadesh\Work\Research Topics\Quantum\Lambda\data\APO100USA_R_20241371500_01H_30S_MO.crx'  # Replace with your RINEX file path
data = gr.load(rinex_file)

# Extract necessary data (this is a simplified example)
# You will need to extract the float ambiguities and their covariance matrix
# For demonstration, let's assume we have the following:
Q = np.array([[2.0, 0.5], [0.5, 1.0]])  # Example covariance matrix
a = np.array([1.2, 0.8])  # Example float ambiguities

# Apply LAMBDA method
a_hat = lambda_method(Q, a)
print("Estimated integer ambiguities:", a_hat)