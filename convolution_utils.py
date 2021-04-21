from sympy.solvers import solve
from sympy import Symbol


def calculate_output_size(w: int, h: int, stride: int, padding: int, kernel_size: int, n_filters: int):
    output_width = (w - kernel_size + 2 * padding) / stride + 1
    output_height = (h - kernel_size + 2 * padding) / stride + 1
    return int(output_width), int(output_height), n_filters


def calculate_filter_size(input_dim: tuple, stride: int, padding: int, desired_dim: tuple):
    input_width, input_height, input_depth = input_dim
    desired_width, desired_height, desired_depth = desired_dim
    x = Symbol('x')
    width_equation = (input_width - x + 2 * padding) / stride + 1 - desired_width
    height_equation = (input_height - x + 2 * padding) / stride + 1 - desired_height
    kernel_width_answer = solve(width_equation)
    kernel_height_answer = solve(height_equation)
    assert len(kernel_width_answer) == 1, 'The solution for kernel width has more than 1 root.'
    assert len(kernel_height_answer) == 1, 'The solution for kernel height has more than 1 root.'
    assert kernel_width_answer[0].is_integer, 'The resulting kernel width is not and integer.'
    assert kernel_height_answer[0].is_integer, 'The resulting kernel height is not and integer.'
    assert kernel_width_answer[0] > 0, 'The resulting kernel width is a negative number.'
    assert kernel_height_answer[0] > 0, 'The resulting kernel height is a negative number.'
    kernel_width = int(kernel_width_answer[0])
    kernel_height = int(kernel_height_answer[0])
    print(f'You will need {desired_depth} filters with size ({kernel_width}, {kernel_height}, {input_depth})')
    return kernel_width, kernel_height, input_depth, desired_depth


print('Output size is:')
inputs = calculate_output_size(99, 99, 1, 3, 5, 3)
print(calculate_filter_size(inputs, 2, 5, (50, 50, 6)))
