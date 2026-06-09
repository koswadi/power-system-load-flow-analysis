def calculate_losses():

    line_losses = {
        "Line 1-2": 0.75,
        "Line 2-3": 0.48,
        "Line 3-4": 0.42,
        "Line 4-5": 0.48
    }

    total_loss = sum(line_losses.values())

    return line_losses, total_loss


if __name__ == "__main__":
    losses, total = calculate_losses()

    print(losses)
    print("Total Loss:", total)