# You are given a list of log entries from a system. Each log entry has the following format: "LEVEL message", where LEVEL is one of INFO, WARNING, ERROR.

# Your task is to compress consecutive identical log entries by adding a repetition counter.

# Rules:
# Only consecutive identical entries should be compressed.
# The comparison must be case-sensitive.
# The original log message must be preserved.
# A single occurrence should remain unchanged.
# Repeated entries should be replaced with the entry followed by " (xN)", where N is the number of repetitions.
# The order of the logs must remain unchanged.
# If the input list is empty, return an empty list.
# Examples
# #### Input
# [
# "ERROR Disk failure",
# "ERROR Disk failure",
# "ERROR Disk failure",
# "INFO User login"
# ]

# #### Output
# [
# "ERROR Disk failure (x3)",
# "INFO User login"
# ]
# Explanation: The three consecutive "ERROR Disk failure" entries are combined into one entry.

# #### Input
# [
# "INFO Connected",
# "WARNING Low battery",
# "INFO Connected"
# ]

# #### Output
# [
# "INFO Connected",
# "WARNING Low battery",
# "INFO Connected"
# ]
# Explanation: Only consecutive identical logs are compressed. The two INFO entries are not next to each other, so they remain separate.


def smart_log_formatter(logs):
    if not logs:
        return []
    
    result = []
    current_log = logs[0]
    count = 1
    
    for i in range(1, len(logs)):
        if logs[i] == current_log:
            count += 1
        else:
            if count == 1:
                result.append(current_log)
            else:
                result.append(f"{current_log} (x{count})")
            
            current_log = logs[i]
            count = 1
    
    if count == 1:
        result.append(current_log)
    else:
        result.append(f"{current_log} (x{count})")
    
    return result