import math
import matplotlib.pyplot as plt

def main():
    # Explaining the program
    print("Hello. This program will calculate the final velocity and the time of a ball that drops based on the given variables: vo, a, and s.")
    
    # Getting the magnitude of gravity
    g = int(input("\nPlease enter the magnitude of gravity: "))
    
    # Getting the height-displacement
    s = int(input("\nPlease enter the height the ball drops from: "))

    #Getting the mass
    m = int(input("\nPlease enter the mass of the ball: "))
    
    # Defining the initial velocity
    vo = 0
    
    # Solving for Vf (final velocity)
    vf = math.sqrt(vo**2 + 2 * g * s)
    print(f"\nThe final velocity is {vf:.2f} m/s.")
    
    # Solving for t (time)
    t = math.sqrt(2 * s / g)
    print(f"\nThe time it took for the ball to drop is {t:.2f} seconds.")

      #The actual values in the velocity vs. Time graph:
    timeIntervals = []
    positions = []
    timeInterval = 0.1
    currentTime = 0.0
    

    #Velocity of the train (in m/s):
    velocityOfTrain = 1

    #Velocity of the ball with respect of the person (in m/s):
    velocityBall = velocityOfTrain + vf

    #displacement of the train with respect to person (in m/s):
    displacementX = velocityOfTrain * t
    
    while currentTime <= t:
        position = s - (0.5 * g * currentTime**2)
        if position <0:
            position = 0
        timeIntervals.append(currentTime)
        positions.append(position)
        currentTime += timeInterval

    #Writing variables and values to a text file
    with open("ballFallingResults.txt", "w") as file:
        file.write("Ball Falling Program Results:\n")
        file.write(f"Inital Velocity (vo): {vo} m/s\n")
        file.write(f"Gravity (g): {g} m/s²\n")
        file.write(f"Initial Height (s): {s} m/n")
        file.write(f"Final Velocity (vf): {vf:.2f} m/s\n")
        file.write(f" Total Time (t): {t:.2f} seconds\n")
        file.write(f"Mass (m): {m} kg\n")
        
        #Tell the user that the textfile has been made and saved.
        print("\nResults have been put into the textfile ballFallingResults.txt.")

        #The velocity vs. time graph to be put into the textfile:
        file.write("\nPosition vs. Time Table:\n")
        file.write(f"{'Time (s)':<10}{'Position (m)':<15}\n")
        file.write("-"* 25 + "\n")
        for time, position in zip(timeIntervals, positions):
            file.write(f"{time:<10.2f}{position:<15.2f}\n")

      
        #Plotting the graph
            plt.figure(figsize=(8,6))
            plt.plot(timeIntervals, positions, label="Position (m)", color = "blue", marker = "o")
            plt.title("Position vs. Time Graph")
            plt.xlabel("Time (seconds)")
            plt.ylabel("Position(m)")
            plt.grid(True)
            plt.legend()
            plt.savefig("positionVsTimeGraph.png")
            plt.close()
                
   
# Run the program
if __name__ == "__main__":
    main()

