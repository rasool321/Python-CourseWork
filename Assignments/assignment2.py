# WhatsApp Chat Data Analysis Assignment

# 1. Count total messages
def total_msgs(msgs):
    return len(msgs)

# 2. Unique users
def unique_users(msgs):
    return {m.split(":")[0] for m in msgs}

# 3. Total words
def total_words(msgs):
    count = 0
    for m in msgs:
        parts = m.split(": ", 1)
        if len(parts) > 1:
            count += len(parts[1].split())
    return count

# 4. Average words per message
def avg_words(msgs):
    return round(total_words(msgs) / len(msgs), 2) if msgs else 0

# 5. Longest message
def longest_msg(msgs):
    return max(msgs, key=len) if msgs else None

# 6. Most active user
def most_active_user(msgs):
    user_count = {}
    for m in msgs:
        usr = m.split(":")[0]
        user_count[usr] = user_count.get(usr, 0) + 1
    if not user_count:
        return None, 0
    top_user = max(user_count, key=user_count.get)
    return top_user, user_count[top_user]

# 7. Messages by a user
def user_msg_count(msgs, usr):
    return sum(1 for m in msgs if m.startswith(usr + ":"))

# 8. Most frequent word by a user
def frequent_word(msgs, usr):
    from collections import Counter
    words = []
    for m in msgs:
        if m.startswith(usr + ":"):
            parts = m.split(": ", 1)
            if len(parts) > 1:
                words.extend(parts[1].lower().split())
    return Counter(words).most_common(1)[0][0] if words else None

# 9. First and last message by a user
def first_last_msg(msgs, usr):
    user_msgs = [m for m in msgs if m.startswith(usr + ":")]
    return (user_msgs[0], user_msgs[-1]) if user_msgs else (None, None)

# 10. Check if user exists
def user_present(msgs, usr):
    return usr in unique_users(msgs)

# 11. Repeated words in chat
def repeated_words(msgs):
    from collections import Counter
    all_words = []
    for m in msgs:
        parts = m.split(": ", 1)
        if len(parts) > 1:
            all_words.extend(parts[1].lower().split())
    return {w for w, c in Counter(all_words).items() if c > 1}

# 13. User with longest average message length
def longest_avg_msg(msgs):
    word_count = {}
    msg_count = {}
    for m in msgs:
        if ": " in m:
            usr, txt = m.split(": ", 1)
            words = len(txt.split())
            word_count[usr] = word_count.get(usr, 0) + words
            msg_count[usr] = msg_count.get(usr, 0) + 1
    if not word_count:
        return None, 0
    avg_lengths = {u: word_count[u] / msg_count[u] for u in word_count}
    top_user = max(avg_lengths, key=avg_lengths.get)
    return top_user, round(avg_lengths[top_user], 2)

# 14. Messages mentioning a user
def mentions_count(msgs, usr):
    return sum(1 for m in msgs if usr.lower() in m.lower())

# 15. Remove duplicate messages
def remove_duplicates(msgs):
    return list(dict.fromkeys(msgs))

# 16. Sort messages alphabetically
def sort_msgs(msgs):
    return sorted(msgs)

# 17. Extract questions
def extract_questions(msgs):
    return [m for m in msgs if "?" in m]

# 18. Reply ratio between two users
def reply_ratio(msgs, u1, u2):
    return sum(1 for i in range(1, len(msgs)) if msgs[i].startswith(u2 + ":") and msgs[i - 1].startswith(u1 + ":"))

# 19. Deleted messages
def deleted_msgs(msgs):
    return sum(1 for m in msgs if m.strip() == "This message was deleted")

# -------- Main Program --------
n = int(input("Enter number of messages: "))
msgs = [input() for _ in range(n)]

while True:
    print("\nOptions:")
    print("1.Total 2.Users 3.Words 4.Avg 5.Longest 6.Active 7.User count 8.Freq word")
    print("9.First/Last 10.Check user 11.Repeated 13.Longest avg 14.Mentions 15.Remove dupes")
    print("16.Sort 17.Questions 18.Reply ratio 19.Deleted 0.Exit")
    ch = int(input("Choose: "))

    if ch == 0:
        print("Exiting...")
        break
    elif ch == 1:
        print("Total messages:", total_msgs(msgs))
    elif ch == 2:
        print("Users:", unique_users(msgs))
    elif ch == 3:
        print("Total words:", total_words(msgs))
    elif ch == 4:
        print("Average words/message:", avg_words(msgs))
    elif ch == 5:
        print("Longest message:", longest_msg(msgs))
    elif ch == 6:
        u, c = most_active_user(msgs)
        print(f"Most active user: {u} ({c} messages)")
    elif ch == 7:
        usr = input("Enter user: ")
        print(f"Messages sent by {usr}:", user_msg_count(msgs, usr))
    elif ch == 8:
        usr = input("Enter user: ")
        word = frequent_word(msgs, usr)
        if word:
            print(f"Most frequent word by {usr}: \"{word}\"")
        else:
            print(f"No messages found for {usr}.")
    elif ch == 9:
        usr = input("Enter user: ")
        first, last = first_last_msg(msgs, usr)
        if first:
            print("First message:", first)
            print("Last message:", last)
        else:
            print(f"No messages found for {usr}.")
    elif ch == 10:
        usr = input("Enter user: ")
        print(f"User '{usr}' is present." if user_present(msgs, usr) else f"User '{usr}' not found.")
    elif ch == 11:
        print("Repeated words:", repeated_words(msgs))
    elif ch == 13:
        u, avg = longest_avg_msg(msgs)
        print(f"Longest average message: {u} (avg {avg} words)")
    elif ch == 14:
        usr = input("Enter user: ")
        print(f"Messages mentioning '{usr}':", mentions_count(msgs, usr))
    elif ch == 15:
        msgs = remove_duplicates(msgs)
        print("Unique messages count:", len(msgs))
    elif ch == 16:
        print("Sorted messages:", sort_msgs(msgs))
    elif ch == 17:
        print("Questions:", extract_questions(msgs))
    elif ch == 18:
        u1 = input("User 1: ")
        u2 = input("User 2: ")
        print(f"Reply ratio from {u2} to {u1}: {reply_ratio(msgs, u1, u2)} replies")
    elif ch == 19:
        print("Deleted messages found:", deleted_msgs(msgs))
    else:
        print("Invalid choice, try again.")