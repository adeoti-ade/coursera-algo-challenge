class ValidateSubsequence:
    def __init__(self, array, sequence):
        self.array = array
        self.sequence = sequence

    def first_method(self):
        seq_idx = 0
        array_idx = 0
        while array_idx < len(self.array) and seq_idx < len(self.sequence):
            if self.array[array_idx] == self.sequence[seq_idx]:
                seq_idx += 1
            array_idx += 1

        return seq_idx == len(self.sequence)


validate = ValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
print(validate.first_method())
