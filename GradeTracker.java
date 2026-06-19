import java.util.ArrayList;
import java.util.Scanner;

public class GradeTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.收藏);
        ArrayList<String> studentNames = new ArrayList<>();
        ArrayList<Double> studentGrades = new ArrayList<>();
        
        System.out.println("=== Student Grade Tracker ===");
        
        while (true) {
            System.out.print("Enter student name (or type 'exit' to finish): ");
            String name = scanner.nextLine();
            
            if (name.equalsIgnoreCase("exit")) {
                break;
            }
            
            System.out.print("Enter grade for " + name + ": ");
            double grade = scanner.nextDouble();
            scanner.nextLine(); // Consume newline character
            
            // Input validation to ensure grade is valid
            if (grade >= 0 && grade <= 100) {
                studentNames.add(name);
                studentGrades.add(grade);
            } else {
                System.out.println("Invalid grade! Please enter a value between 0 and 100.");
            }
            System.out.println();
        }
        
        // Check if any data was entered
        if (studentNames.isEmpty()) {
            System.out.println("No student records entered.");
            return;
        }
        
        // Calculations
        double total = 0;
        double highest = studentGrades.get(0);
        double lowest = studentGrades.get(0);
        String highestStudent = studentNames.get(0);
        String lowestStudent = studentNames.get(0);
        
        for (int i = 0; i < studentGrades.size(); i++) {
            double currentGrade = studentGrades.get(i);
            total += currentGrade;
            
            if (currentGrade > highest) {
                highest = currentGrade;
                highestStudent = studentNames.get(i);
            }
            
            if (currentGrade < lowest) {
                lowest = currentGrade;
                lowestStudent = studentNames.get(i);
            }
        }
        
        double average = total / studentGrades.size();
        
        // Display Summary Report
        System.out.println("\n=================================");
        System.out.println("         SUMMARY REPORT          ");
        System.out.println("=================================");
        for (int i = 0; i < studentNames.size(); i++) {
            System.out.printf("%-15s : %.2f\n", studentNames.get(i), studentGrades.get(i));
        }
        System.out.println("---------------------------------");
        System.out.printf("Total Students : %d\n", studentNames.size());
        System.out.printf("Average Score  : %.2f\n", average);
        System.out.printf("Highest Score  : %.2f (%s)\n", highest, highestStudent);
        System.out.printf("Lowest Score   : %.2f (%s)\n", lowest, lowestStudent);
        System.out.println("=================================");
        
        scanner.close();
    }
          }
