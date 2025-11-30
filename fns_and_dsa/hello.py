# First-Fit algorithm implementation

# Function which allocates memory to blocks using First fit
def processFirstFit(size_of_block, m, size_of_process, n):
    # Register the block id of the block allocated to a process
    allocation = [-1] * n

    # Select a process and assign it to the first most suitable block
    for i in range(n):
        for j in range(m):
            if size_of_block[j] >= size_of_process[i]:
                # Allocate block j to process i
                allocation[i] = j

                # Reduce available memory in this block
                size_of_block[j] -= size_of_process[i]

                # Move to the next process
                break

    # Print the allocation result
    print("Process No.  Process Size  Block No.")
    for i in range(n):
        print(f"{i + 1:<12}{size_of_process[i]:<13}", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


# Main code block
if __name__ == '__main__':
    size_of_block = [200, 600, 100, 300, 700]
    size_of_process = [312, 417, 132, 526]
    m = len(size_of_block)
    n = len(size_of_process)

    processFirstFit(size_of_block, m, size_of_process, n)
