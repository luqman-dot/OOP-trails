import math

def normal_pdf(x, mu, sigma):
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Example: Mean = 0, Standard Deviation = 1, for x = 1
print(f"Normal PDF: {normal_pdf(1, 0, 1):.4f}")
