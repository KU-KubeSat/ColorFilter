from filtercolor import *

def main():
    filaname = 'KUbesat color filter\kubesattest2.png'
    lower_1 = np.array([25, 30, 30])   # Lower bound of color 1 in HSV
    upper_1 = np.array([95, 255, 255]) # Upper bound of color 1 in HSV
    lower_2 =  np.array([0, 30, 30]) # Upper bound of color 2 in HSV
    upper_2 = np.array([15,255,255]) # Upper bound of color 2 in HSV



    file1=filter_color(filaname, lower_1, upper_1, output_path='kubesatfilter1.png')
    file2=filter_color(filaname, lower_2, upper_2, output_path='kubesatfilter2.png')
main()