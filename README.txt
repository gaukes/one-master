VIZAG ONE (abbr. one) collected information for application here. There are two main folders: one-api
and one-website. These two run separtely but are connected by a REST api. The website can connect to
the local server via HTTP requests. Information regarding each folder below:

one-api:
    1.) Must be run through the terminal.
    2.) First, execute "chmod +x install.sh" from that folder.
    3.) If you don't have python and pip install that first.
        a.) You can check if you have these with:
            "pip --version" (command not found means it doesn't exist)
            "python --version"
    3.) Execute "./install.sh" to let script install needed tools and directories.
    4.) Execute "./run.sh" to start the server
    5.) Can test with "./test.sh" after server is running. Refer to this to see what different REST
        calls do.

one-website:
    1.) Open index.html. Can double click or execute "open index.html" in terminal.
    2.) Page refreshes ever second. Temporary fix (might change later).
    3.) If you make a rest api call to increase points of Tom Cruise during this time with
        "curl -i -H "Content-Type: application/json" -X PUT -d '{"points":1}' http://localhost:5000/one/api/v1.0/points/3"
        you should see a change on the website when it refreshes.

Server is done for the most part. Could add mongodb database to store information between runs (if
necessary). Dynamic part of website is mostly done but it needs to be prettyfied.
