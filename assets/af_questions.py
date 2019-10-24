from collections import namedtuple

# Set the object type "Question" as a Named Tuple, enabling us to call it section by section in the main program
Question = namedtuple("Question", "question choices correct")

# Create the Question objects and ensure each one has a different variable name so they can be referenced by the Opponent objects
# All the questions that belong to the Solutions Architect Associate Course
af_questions =  [

    # Practice exam question 3
    Question("""Your company plans to move several servers to Azure.
The company's compliance policy states that a server named FinServer must be on a separate network segment.
You are evaluating which Azure services can be used to meet the compliance policy requirements.

Which Azure solution should you recommend?""", 
    # The possible answers
    [
        "A resource group for FinServer and another resource group for all the other servers.", 
        "A virtual network for FinServer and another virtual network for all the other servers.", 
        "A VPN for FinServer and a virtual network gateway for each other server.", 
        "One resource group for all the servers and a resource lock for FinServer."
    ], 
    # The correct answer
    "b"), 

    # Practice exam question 4
    Question("""You plan to map a network drive from several computers that run Windows 10 to Azure Storage. 
You need to create a storage solution in Azure for the planned mapped drive.

What should you create?""", 
    # The possible answers
    [
        "An Azure SQL database", 
        "A virtual machine data disk", 
        "A Files service in a storage account", 
        "A Blobs service in a storage account"], 
    # The correct answer
    "c"),

    # Practice exam question 6
    Question("""Your company plans to migrate all its network resources to Azure.
You need to start the planning process by exploring Azure.

What should you create first?""", 
    # The possible answers
    [
        "A subscription", 
        "A resource group", 
        "A virtual network", 
        "A management group"
    ], 
    # The correct answer
    "a"),

    # Practice exam question 7
    Question("""You have an on-premises application that sends email notifications automatically based on a rule.
You plan to migrate the application to Azure.
You need to recommend a serverless computing solution for the application.

What should you include in the recommendation?""", 
    # The possible answers
    [
        "A web app", 
        "A server image in Azure Marketplace", 
        "A logic app", 
        "An API app"], 
        # The correct answer
        "c"),

    # Practice exam question 8
    Question("""You plan to deploy a website to Azure. The website will be accessed by users worldwide and will host large video files.
You need to recommend which Azure feature must be used to provide the best video playback experience.

What should you recommend?""", 
    # The possible answers
    [
        "An application gateway", 
        "An Azure ExpressRoute circuit", 
        "A content delivery network (CDN)", 
        "An Azure Traffic Manager profile"], 
        # The correct answer
        "c"),

    # Practice exam question 13
    Question("""Your company plans to deploy an Artificial Intelligence (AI) solution in Azure.

What should the company use to build, test, and deploy predictive analytics solutions?""", 
    # The possible answers
    [
        "Azure Logic Apps", 
        "Azure Machine Learning Studio", 
        "Azure Batch", 
        "Azure Cosmos DB"], 
        # The correct answer
        "b")  
]