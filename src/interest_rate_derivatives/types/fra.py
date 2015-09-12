class Fra:
    def __init__(self, r1, r2, tau1, tau2, basis):
        self.r1 = r1
        self.r2 = r2
        self.tau1 = tau1
        self.tau2 = tau2
        self.basis = basis

    def get_value(self):
        return (((1 + self.r2 * self.tau2 / self.basis) / (1 + self.r1 * self.tau1 / self.basis)) - 1) * (
        self.basis / (self.tau2 - self.tau1))
