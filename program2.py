def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create a DP table with dimensions (m + 1) x (n + 1), initialized to False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Handle cases where the pattern starts with '*' (can match empty string)
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # Characters match or '?' can replace any single character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero characters (dp[i][j-1]) or one/more characters (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            else:
                # Characters do not match
                dp[i][j] = False

    return dp[m][n]

# Example usage
print(decode_message("aa", "a"))      # Output: False
print(decode_message("aa", "*"))      # Output: True
print(decode_message("cb", "?a"))     # Output: False
