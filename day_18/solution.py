def process_operation(expression: str):
    operators_position = [m.start() for m in re.finditer(r'\+|\*', expression)]

    if len(operators_position) == 0:
        return expression
    if len(operators_position) == 1:
        return str(eval(expression))
    else:
        second_operator = operators_position[1]
        eval_string = expression[0:second_operator]

        partial = str(eval(eval_string))
        rest = expression[second_operator::]

        expression = partial + rest

        result = process_operation(expression)
        return result


def process(expression):
    opening = [m.start() for m in re.finditer(r'\(', expression)]
    closing = [m.start() for m in re.finditer(r'\)', expression)]

    if len(opening) == 0:
        return process_operation(expression)
    else:
        for o_position in opening[::-1]:
            for c_position in closing:
                if o_position < c_position:
                    selected = expression[o_position + 1:c_position]
                    inner_result = process_operation(selected)
                    expression = expression[0:o_position] + inner_result + expression[c_position + 1::]
                    return process(expression)


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        raw_data = f.read().splitlines()

    results = []
    for expression in raw_data:
        result = process(expression)
        results.append(int(result))
    print(sum(results))
