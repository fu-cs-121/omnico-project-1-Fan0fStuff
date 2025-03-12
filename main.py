# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            line = line.strip()

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]

            # TODO: Define session_duration and happiness_rating variables and convert them to integers
            # Hint: Use the int() function to convert strings to integers
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
        for algorithm, data in stats.items():
            if data['session_count'] > 0:
                data['avg_happiness'] = data['total_happiness'] // data['session_count']
                data['avg_duration'] = data['total_duration'] // data['session_count']
            else:
                print("invalid numbers")
    #  V - Calculate avg_duration = total_duration / session_count 
    #  V - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration' 

    # TODO: Determine the algorithm with the highest average happiness rating
        #determine the algorithm with the highest average happiness rating
        highest_avg_happiness = 0
        happiest_algorithm = ""
        for algorithm, data in stats.items():
            if data['avg_happiness'] > highest_avg_happiness:
                highest_avg_happiness = data['avg_happiness']
                happiest_algorithm = algorithm 
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values

    # TODO: Determine the algorithm with the longest average session duration
        longest_sesh_duration = 0
        longest_algorithm = ""
        for algorithm, data in stats.items():
            if data['avg_duration'] > longest_sesh_duration:
                longest_sesh_duration = data['avg_duration']
                longest_algorithm = algorithm
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values
        
    # TODO: Print the report
    print("Euphoria User Engagement Analysis Report")
    print("----------------------------------------")

    print("\nAverage Happiness Rating per Algorithm:")
    for algorithm, data in stats.items():
        print(f"- {algorithm}: {data['avg_happiness']}")
    print("\nTotal Number of Sessions per Algorithm:")
    for algorithm, data in stats.items():
        print(f"- {algorithm}: {data['avg_duration']}")
    print("\nAverage Session Duration per Algorithm:")
    for algorithm, data in stats.items():
        print(f"- {algorithm}: {data['session_count']} minutes")
    print("\nHighest Average Happiness Rating:")
    for algorithm, data in stats.items():
        print(f"- {algorithm}: {data['avg_duration']}")
    print("\nHighest Average Happiness Rating:")
    print(f"- {happiest_algorithm} with an average happiness rating of {highest_avg_happiness}")
    print("\nLongest Average Session Duration:")
    for algorithm, data in stats.items():
        print(f"- {longest_algorithm} with an average session duration of {longest_sesh_duration} minutes")

    


    # - JoyStream: 8.50
    # - SerenityFlow: 7.00
    # - DeepPulse: 5.00

    # Total Number of Sessions per Algorithm:
    # - JoyStream: 4
    # - SerenityFlow: 3
    # - DeepPulse: 3

    # Average Session Duration per Algorithm:
    # - JoyStream: 37.50 minutes
    # - SerenityFlow: 30.00 minutes
    # - DeepPulse: 45.00 minutes

    # Highest Average Happiness Rating:
    # - JoyStream with an average happiness rating of 8.50

    # Longest Average Session Duration:
    # - DeepPulse with an average session duration of 45.00 minutes

    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output

if __name__ == "__main__":
    main()