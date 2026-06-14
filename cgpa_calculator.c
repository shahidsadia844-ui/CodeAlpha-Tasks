#include <stdio.h>

int main() {
    int num_courses;
    double total_credits = 0.0;
    double total_grade_points = 0.0;
    double cgpa;

    printf("--- CGPA Calculator ---\n\n");

    // 1. Total courses ki ginti input lena
    printf("Total kitne courses hain? ");
    scanf("%d", &num_courses);

    // Data store karne ke liye arrays
    double grades[num_courses];
    int credit_hours[num_courses];

    // 2. Har course ka data loop ke zariye lena
    for (int i = 0; i < num_courses; i++) {
        printf("\nCourse %d ka Grade Point (e.g., 4.0, 3.7, 3.0): ", i + 1);
        scanf("%lf", &grades[i]);

        printf("Course %d ke Credit Hours (e.g., 3, 4): ", i + 1);
        scanf("%d", &credit_hours[i]);

        // Total calculation sath sath karna
        total_grade_points += (grades[i] * credit_hours[i]);
        total_credits += credit_hours[i];
    }

    // 3. Formula apply karke CGPA nikalna
    if (total_credits > 0) {
        cgpa = total_grade_points / total_credits;
    } else {
        cgpa = 0.0;
    }

    // 4. Final Result display karna
    printf("\n=====================================\n");
    printf("           MARK SHEET / RESULT        \n");
    printf("=====================================\n");
    printf("Course\t\tGrade\t\tCredit Hours\n");
    printf("-------------------------------------\n");
    
    for (int i = 0; i < num_courses; i++) {
        printf("Course %d\t%.2lf\t\t%d\n", i + 1, grades[i], credit_hours[i]);
    }

    printf("-------------------------------------\n");
    printf("Total Credit Hours: %.0lf\n", total_credits);
    printf("Aapka Final CGPA hai: %.2lf\n", cgpa);
    printf("=====================================\n");

    return 0;
}
