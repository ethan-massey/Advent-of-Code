lines = open("data.txt", "r").readlines()

reports = []
for line in lines:
    report = [int(i) for i in line.split(" ")]
    reports.append(report)


def is_safely_increasing(report, is_second_attempt) -> bool:
    for i in range(1, len(report)):
        if report[i] <= report[i - 1] or not is_safe_jump(report[i], report[i - 1]):
            if is_second_attempt:
                return False
            else:
                fixed_a = remove_index_from_report(report, i)
                fixed_b = remove_index_from_report(report, i - 1)
                return is_safely_increasing(fixed_a, True) or is_safely_increasing(
                    fixed_b, True
                )
    return True


def is_safely_decreasing(report, is_second_attempt) -> bool:
    for i in range(1, len(report)):
        if report[i] >= report[i - 1] or not is_safe_jump(report[i], report[i - 1]):
            if is_second_attempt:
                return False
            else:
                fixed_a = remove_index_from_report(report, i)
                fixed_b = remove_index_from_report(report, i - 1)
                return is_safely_decreasing(fixed_a, True) or is_safely_decreasing(
                    fixed_b, True
                )
    return True


def is_safe_jump(num1, num2) -> bool:
    diff = abs(num1 - num2)
    return 1 <= diff <= 3


def remove_index_from_report(report, index) -> list:
    return report[:index] + report[index + 1 :]


# part 1
safe_reports = []
for report in reports:
    if is_safely_decreasing(report, True) or is_safely_increasing(report, True):
        safe_reports.append(report)

print(len(safe_reports))

# part 2
safe_reports = []
for report in reports:
    if is_safely_decreasing(report, False) or is_safely_increasing(report, False):
        safe_reports.append(report)

print(len(safe_reports))
