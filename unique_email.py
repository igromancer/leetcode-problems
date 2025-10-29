def trim_email(email: str) -> str:
    local, domain = email.split("@")
    local_trimmed = ""
    for l in local:
        if l != "." and l != "+":
            local_trimmed += l
        elif l == ".":
            continue
        else:
            break
    return local_trimmed + "@" + domain


def numUniqueEmails(emails: list[str]) -> int:
    unique = set()
    for e in emails:
        unique.add(trim_email(e))
    return len(unique)


print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))