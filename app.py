import tkinter as tk
import pandas as pd

def submit_job_description():
    job_title = job_title_entry.get()
    qualification = qualification_entry.get()
    skills = skills_entry.get()
    work_experience = work_experience_entry.get()

    # Create a dictionary with the job description data
    job_description = {
        'Job Title': [job_title],
        'Qualification': [qualification],
        'Skills': [skills],
        'Work Experience': [work_experience]
    }

    # Load existing data from the Excel file, if any
    try:
        df = pd.read_excel('job_descriptions.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame()

    # Append the new job description to the existing data
    df = pd.concat([df,pd.DataFrame(job_description)], ignore_index=True)

    # Save the updated data to the Excel file
    df.to_excel('job_descriptions.xlsx', index=False)

    # Reset the entry fields after submission
    job_title_entry.delete(0, tk.END)
    qualification_entry.delete(0, tk.END)
    skills_entry.delete(0, tk.END)
    work_experience_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Job Description")
window.geometry("800x400")
window.configure(bg="#F9F7F6")

# Load the background image
background_image = tk.PhotoImage(file="resume_background.png")

# Create a canvas to display the background image
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Create labels for each input field
job_title_label = tk.Label(window, text="Job Title:", bg="#F9F7F6", fg="#333", font=("Arial", 14, "bold"))
job_title_label.place(x=50, y=50)
qualification_label = tk.Label(window, text="Qualification:", bg="#F9F7F6", fg="#333", font=("Arial", 14, "bold"))
qualification_label.place(x=50, y=100)
skills_label = tk.Label(window, text="Skills:", bg="#F9F7F6", fg="#333", font=("Arial", 14, "bold"))
skills_label.place(x=50, y=150)
work_experience_label = tk.Label(window, text="Work Experience:", bg="#F9F7F6", fg="#333", font=("Arial", 14, "bold"))
work_experience_label.place(x=50, y=200)

# Create entry fields for each input
job_title_entry = tk.Entry(window, bg="#FFFFFF", fg="#333", font=("Arial", 14), width=40)
job_title_entry.place(x=250, y=50)
qualification_entry = tk.Entry(window, bg="#FFFFFF", fg="#333", font=("Arial", 14), width=40)
qualification_entry.place(x=250, y=100)
skills_entry = tk.Entry(window, bg="#FFFFFF", fg="#333", font=("Arial", 14), width=40)
skills_entry.place(x=250, y=150)
work_experience_entry = tk.Entry(window, bg="#FFFFFF", fg="#333", font=("Arial", 14), width=40)
work_experience_entry.place(x=250, y=200)

# Create a button to submit the job description
submit_button = tk.Button(window, text="Submit", command=submit_job_description, bg="#00A388", fg="#FFFFFF", font=("Arial", 14, "bold"))
submit_button.place(x=350, y=250)

# Run the GUI event loop
window.mainloop()