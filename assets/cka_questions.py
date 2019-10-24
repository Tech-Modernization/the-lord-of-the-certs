from collections import namedtuple

# Set the object type "Question" as a Named Tuple, enabling us to call it section by section in the main program
Question = namedtuple("Question", "question choices correct")

# Create the Question objects and ensure each one has a different variable name so they can be referenced by the Opponent objects
# All the questions that belong to the Solutions Architect Associate Course
cka_questions =  [

    Question("""What type of Kubernetes resource would you use to expose a deployment?""", 
    # The possible answers
    [
        "Secret", 
        "Configmap", 
        "Service", 
        "Pod"], 
    # The correct answer
    "c"),

   Question("""ETCD is a consistent and highly-available key value store used to store Kubernetes cluster data.
   
True or False?""", 
    # The possible answers
    [
        "True", 
        "False"], 
        # The correct answer
        "a"),

    Question("""The 'Kube-scheduler' is a component of the Kubernetes control plane that exposes the Kubernetes API.
    The API server is the front end for the Kubernetes control plane.
    
    True or False?""", 
    # The possible answers
    [
        "True", 
        "False"
    ], 
    # The correct answer
    "b"),

    Question("""Which service resource would cost money if running on a public cloud?""", 
    # The possible answers
    [
        "ClusterIP", 
        "NodePort", 
        "LoadBalancer"], 
        # The correct answer
        "c"),

    Question("""Which command would you use to create a pod?""", 
    # The possible answers
    [
        "kubectl create nginx --image=nginx", 
        "kubectl create nginx --image=nginx --restart=Never", 
        "kubectl create pod --image=nginx"], 
        # The correct answer
        "b"),

    Question("""What is 'Kubelet'?""", 
    # The possible answers
    [
        "The container runtime", 
        "The network proy that runs each node", 
        "An agent that runs on each node in the cluster to ensure containers are running in a pod",
        "An agent that runs on each node in the cluster to ensure that the node is healthy"], 
        # The correct answer
        "c")
]