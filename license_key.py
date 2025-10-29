def licenseKeyFormatting(s: str, k: int) -> str:
    result = []
    group = ""
    x = s.replace("-", "").upper()
    for i in range(len(x)-1, -1, -1):
        group += x[i]
        if len(group) == k:
            result.append(group[::-1])
            group = ""
    if group:
        result.append(group[::-1])
    result.reverse()
    return "-".join(result)


print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
