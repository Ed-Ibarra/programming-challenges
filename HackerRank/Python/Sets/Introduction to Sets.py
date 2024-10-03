"""
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used:
        AVERAGE = Sum Of Distinct Heights / Total Number of Distinct Heights

/

La Sra. Gabriel Williams es profesora de botánica en el District College. Un día, le pidió a su estudiante Mickey que calculara el promedio de todas las plantas con distintas alturas en su invernadero.
Fórmula utilizada:
        PROMEDIO = Suma de alturas distintas / Número total de alturas distintas
--------------------------------------------------------------------------------
* Sample Input
10
161 182 161 154 176 170 167 171 170 174  

? Sample Output
169.375
--------------------------------------------------------------------------------
! Explanation:
! Here, set ([154, 161, 167, 170, 171, 174, 176, 182]) is the set containing the distinct heights.
! Using the sum() and len() functions, we can compute the average.
! Average = 1355 / 8 = 169.375

"""
# Function to return the average = Sum Of Distinct Heights / Total Number of Distinct Heights
def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    
    print(average(arr))