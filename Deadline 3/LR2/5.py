def filter_logs(log_lst, keyword):
    for log in log_lst:
        if keyword in log:
            yield log


if __name__ == "__main__":
    logs = [
        "INFO: Server started",
        "ERROR: Database connection failed",
        "INFO: User logged in",
        "ERROR: File not found"
    ]

    for error in filter_logs(logs, "ERROR"):
        print(error)