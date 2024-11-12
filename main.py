import os
   
def main():
    print("Welcome to the Digital Signal Processing Program")
    input_signal=input("Enter the signal you want to give as input:\n1.Analog Signal\n2. Digtal Signal\n")
    if(int(input_signal)==1):
        print("\nYou have chosen Analog Signal\n")
        modulation_technique=input("Enter the modulation technique you want to use:\n1.Pulse Code Modulation(PCM)\n2.Delta Modulation(DM)\n")
        if int(modulation_technique) == 1:
            os.system("python3 pcm.py")
        else:
            os.system("python3 dm.py")
    else:
        print("\nYou have chosen Digital Signal\n")
        line_encoding_technique=int(input("Enter the encoding technique you want to implement:\n1.NRZ_L\n2.NRZ_I\n3.Manchester\n4.Differential Manchester\n5.AMI\n"))
        if line_encoding_technique==1:
            os.system("python3 nrzl.py")
        elif line_encoding_technique==2:
            os.system("python3 nrzi.py")
        elif line_encoding_technique==3:
            os.system("python3 manchester.py")
        elif line_encoding_technique==4:
            os.system("python3 differntial.py")
        else:
            ami_type=int(input("Choose AMI: \n1. with Scrambling\n2. without Scrambling\n"))
            if ami_type==1:
                scramble=int(input("Which type of scrambling:\n1. B8ZS \n2. HDB3\n"))
                if scramble==1:
                    os.system("python3 B8ZS.py")
                else:
                    os.system("python3 HDB3.py")
            else:
                os.system("python3 ami.py")


if __name__ == "__main__":
    main()