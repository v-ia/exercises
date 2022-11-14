# Task: https://ibb.co/cgsQFvn

def employee_stat():
    employees = dict()
    while True:
        try:
            line_list = input().split()
            hours = int(line_list.pop())
            name = ' '.join(line_list)
            employees[name] = employees.get(name, [])
            employees[name].append(hours)
        except EOFError:    # Press Ctrl+D/Cmd+D or Ctrl+Z to finish input and get results
            for name, hours in employees.items():
                work_time = sum(hours)
                print(f'{name}:', *hours, f'; sum: {work_time}')
            break


if __name__ == '__main__':
    employee_stat()
