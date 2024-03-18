class Vector:
    def __init__(self, cordinats: list):

        if not isinstance(cordinats, list):
            raise ValueError("Неправильно задані атрибути")

        self.cordinats = cordinats


    def __repr__(self):

        return f"Vector({self.cordinats})"

    def dim(self):

        return len(self.cordinats)


    def norm(self):

        norm = 0
        for el in self.cordinats:
            norm += el ** 2

        return norm ** 0.5

    def arifmetic_average(self):
        sum = 0

        for el in self.cordinats:
            sum += el

        return sum / self.dim()

    def max_component(self):
        if len(self.cordinats) == 0:
            return 0
        else:
            return max(self.cordinats)

    def min_component(self):
        if len(self.cordinats) == 0:
            return 0
        else:
            return min(self.cordinats)

def vector_generator(line: str):
    line = line.split()
    converted_params = [int(el) for el in line]

    return Vector(converted_params)


def max_dim(vectors: list):
    dims = [int(vector.dim()) for vector in vectors]

    max_dim = max(dims)
    max_dims = []

    for vector in vectors:
        if vector.dim() == max_dim:
            max_dims.append(vector)
        else:
            pass

    if len(max_dims) == 1:
        return max_dims[0]
    else:
        norms = [int(vector.norm()) for vector in max_dims]
        min_norm = min(norms)
        for vector in max_dims:
            if int(vector.norm()) == min_norm:
                return vector
            else:
                pass

def max_norm(vectors: list):
    norms = [int(vector.norm()) for vector in vectors]

    max_norm = max(norms)
    max_norms = []

    for vector in vectors:
        if int(vector.norm()) == max_norm:
            max_norms.append(vector)
        else:
            pass

    if len(max_norms) == 1:
        return max_norms[0]
    else:
        dims = [int(vector.dim()) for vector in max_norms]
        min_dim = min(dims)
        for vector in max_norms:
            if int(vector.dim()) == min_dim:
                return vector
            else:
                pass

def average(vectros: list):
    sum = 0
    for vector in vectors:
        sum += vector.norm()

    return sum / len(vectors)

def max_maximal(vectors: list):
    max_values = [vector.max_component() for vector in vectors]
    max_max = max(max_values)
    max_maximal_values = []
    for vector in vectors:
        if vector.max_component() == max_max:
            max_maximal_values.append(vector)
        else:
            pass

    if len(max_maximal_values) == 1:
        return max_maximal_values[0]
    else:
        min_values = [vector.min_component() for vector in max_maximal_values]
        min_min = min(min_values)
        for vector in max_maximal_values:
            if int(vector.min_component()) == min_min:
                return vector
            else:
                pass

def min_minimal(vectors: list):
    min_values = [vector.min_component() for vector in vectors]
    min_min = max(min_values)
    min_minimal_values = []

    for vector in vectors:
        if vector.min_component() == min_min:
            min_minimal_values.append(vector)
        else:
            pass

    if len(min_minimal_values) == 1:
        return min_minimal_values[0]
    else:
        max_values = [vector.max_component() for vector in min_minimal_values]
        max_max = max(max_values)
        for vector in min_minimal_values:
            if vector.max_component() == max_max:
                return vector
            else:
                pass



if __name__ == "__main__":
    vectors = []

    with open("input01.txt", 'r') as file:
        for line in file:
            try:
                if line == '':
                    break
                else:
                    vectors.append(vector_generator(line))
            except ValueError:
                pass

    print(max_dim(vectors))
    print(max_norm(vectors))
    print(average(vectors))
    print(max_maximal(vectors))
    print(min_minimal(vectors))