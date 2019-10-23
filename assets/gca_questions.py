from collections import namedtuple

# Set the object type "Question" as a Named Tuple, enabling us to call it section by section in the main program
Question = namedtuple("Question", "question choices correct")

# Create the Question objects and ensure each one has a different variable name so they can be referenced by the Opponent objects
# All the questions that belong to the Solutions Architect Associate Course
gca_questions =  [

    Question("""You are working on a project called 'contino', and want to list all the roles assigned to users in the project.
    
Which of the following gcloud commands would you use?""", 
    # The possible answers
    [
        "gcloud iam list contino", 
        "gcloud projects list contino", 
        "gcloud projects get-iam-policy contino", 
        "gcloud iam get-iam-policy contino"
    ], 
    # The correct answer
    "c"), 

    Question("""You're working for a company as a Cloud Engineer. You have a managed instance group for which the autoscaling is
enabled if CPU utilisation is 70%. Right now there are 4 instance available in this instance group. When you connect to one 
of the instances, you can see the CPU utilisation is 75% and there are no new instances starting.

What could be the possible reason for not starting another instance here?""", 
    # The possible answers
    [
        "It will take 60 seconds to launch a new instance.", 
        "Autoscaling is not active.", 
        "Average CPU usage of the instance group is less than 70%.", 
        "None of the above."
    ], 
    # The correct answer
    "c"), 

    Question("""You have been asked by a client to build a backend using Clojure and host it on Google Cloud with full freedom
of choosing OS, applications, libraries etc.

Which Google Cloud service will you use?""", 
    # The possible answers
    [
        "Compute Engine", 
        "App Engine Standard", 
        "Cloud Function", 
        "CloudRun"], 
    # The correct answer
    "a"),

    Question("""You have been hired by a client who is planning to containerize their existing applications in such a way that
they can perform a lift and shift very easily in the future if they plan to move away from Google Cloud.

Which service will best suit this case?""", 
    # The possible answers
    [
        "Cloud Function", 
        "App Engine Standard", 
        "Kubernetes Engine", 
        "CloudRun"
    ], 
    # The correct answer
    "c"),

    Question("""You are about to start working on a micro-service deployment project using Google Kubernetes Engine service. 
The client needs everything on Google and wants you to maintain both frontend and backend code on Google Cloud as well.
    
Which service best suites this case?""", 
    # The possible answers
    [
        "Cloud Storage", 
        "Cloud Source Repository", 
        "Google Container Registry", 
        "GitHub"], 
        # The correct answer
        "b"),

    Question("""You are working as a Systems Administrator and have been asked to make sure that all images are patched up to date 
and developers are not allowed to use old images with are not up to date, in order to comply with PCI.

How would you achieve this?""", 
    # The possible answers
    [
        "Drop an email to all the developers instructing which images to use whenever you patch going forwards.", 
        "Mark images as deprecated to prevent users from deploying from the old images.", 
        "Mark images as obselete to prevent users from deploying from the old images.", 
        "None of the above."], 
        # The correct answer
        "c"),

    Question("""You are building an architecure for one of your clients with a requirement of streaming millions of requests
with high availability and durability along with HIPPA compliance.
    
Which managed service will you prefer?""", 
    # The possible answers
    [
        "Cloud Function", 
        "Cloud DataProc", 
        "Cloud Pub/Sub", 
        "RabbitMQ"], 
        # The correct answer
        "c"),  

    Question("""You have been asked to deploy a highly available Kubernetes cluster using Google Kubernetes Engine by
your manager While spinning up the cluster you realise you do not see the option to create a master.
    
What is the reason for this?""", 
    # The possible answers
    [
        "GKE does not use master nodes to control child nodes.", 
        "You need to spin up a compute instance and set it up as the master node.", 
        "The master nodes are reated automatuically by GKE", 
        "None of the above"], 
        # The correct answer
        "c")  
]