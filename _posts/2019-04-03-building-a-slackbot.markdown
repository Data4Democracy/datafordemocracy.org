---
layout: post
title:  Building a Slackbot
date:   2019-04-02 09:49:00
images: ../../../../../images/blog/head-img.jpg
excerpt:
  Slackbot stuff
categories: Slackbot
---

# Building a Slackbot with Hubot

A chatbot is an invaluable tool for a growing community. Through this article we will go over how to get started with a powerful chatbot framework called hubot. We will then go over how to write commands and a welcome message tailored to your community. Then, after we have everything just how we want it we will add our bot to a slack workspace and deploy it to Heroku. This is written with a beginner in mind so if you are unfamiliar with any of this technology we will be going over it in a way that has a total beginner in mind.

You will need to begin by installing node.js if you have not. You can find the file here [https://nodejs.org/en/download/](https://nodejs.org/en/download/). Once you have node installed you will need npm, you can open your terminal and type `npm install install` to get npm. The last thing you will need to install is a package called yo which is used to create a hubot. You will need to run `npm install -g yo generator-hubot` for this. You can learn more about "yo" here [https://yeoman.io/](https://yeoman.io/). Now that we have our requirements installed we are ready to begin.

![Screenshot](../../../../../images/blog/Screen_Shot_2019-03-26_at_7-84e55fe7-ac00-463f-a02c-197765cdf352.40.45_AM.png){:class="img-responsive"}

To create a new hubot you will need to run the command `yo hubot --adapter=slack` in your terminal. Make sure you are in the directory you would like the bot created in when you run this command. You will then be asked a series of questions. The only really important one here is when you are prompted for the bot adapter, make sure slack is selected. This is just to help our bot communicate with the Slack api. After the install is completed you will just be left with your folder, but now it is full of things that help hubot to run. Lets open this folder in an IDE to continue.

Once we have this  open in our text editor we should see a folder structure like this.

If you view the [README.md](http://readme.md) you will find information on getting the bot started and helpful tips and resources.

For the purposes of this guide we will be working in the `scripts` folder. You can refer to the hubot docs for clarification on the other files. [https://hubot.github.com/docs/](https://hubot.github.com/docs/)

![](../../../../../images/blog/Screen_Shot_2019-03-26_at_2-fdd3b784-cafc-4b10-a905-7504753781a8.32.30_PM.png)

### Built in Help

We will begin our exploration of hubot by opening the scripts folder and then the `example.coffee` file. This file is a great way to familiarize yourself with hubot. The majority of this file is commented out by default to prevent these commands to run, but each one presents a different function of hubot. I would recommend spending time reading over these files, just by reading over you can start to get an idea of how hubot works.

## Breaking down a hubot script

**Part 1 - Description**

At the top of the file you will see 9 lines of commented out code. This is an important format to take note of because you can use this to generate your help commands later.

    # Description:
    #   Example scripts for you to examine and try out.
    #
    # Notes:
    #   They are commented out by default, because most of them are pretty silly and
    #   wouldn't be useful and amusing enough for day to day huboting.
    #   Uncomment the ones you want to try and experiment with.
    #
    #   These are from the scripting documentation: https://github.com/github/hubot/blob/master/docs/scripting.md

    module.exports = (robot) ->

       robot.hear /badger/i, (res) ->
         res.send "Badgers? BADGERS? WE DON'T NEED NO STINKIN BADGERS"

**Part 2 - export**

Next you will see `module.exports = (robot) →`

This command is in the script file to export the what is inside so that hubot can use it.

**Part 3 - functions**

Next you will see a simple function. Lets break it down into smaller parts.

`robot.hear` allows our robot to hear what is going on in the room it is in.

`/badger/i,` This is what the robot is listening for.

`res.send` this is the response that our robot will send when it hears what we are listening for.

Using these basic pieces we have enough information to create all the keyword commands that we want.  Lets get started by creating a new file named `commands.coffee` inside our scripts folder.

Next we will add our description.

    # Description:
    #   To demonstrate basic keyword commands
    #
    # Dependencies:
    #   None
    #
    # Configuration:
    #   None
    #
    # Commands:
    #   hubot hello - Say hello!
    #   hubot !new members - link to procedure for new members.

Next we need our export and function.

    module.exports = (robot) ->
    	robot.hear /hello/i, (res) ->
    		res.send "Hello World"

This function will listen for anyone to say hello and then say "Hello World"

 One way to keep your content up to date is to manage it on a platform like Notion, Github, or Google Docs and then link to that document. This will encourage collaboration and allow you to change your content without having to update your bot.

Lets create a function so that whenever our bot hears "!new members" it will send a link that provides all the information for new members to get started.

    module.exports = (robot) ->
    	robot.hear /!new members/i, (res) ->
    		res.send "https://www.notion.so/dstarling/Click-me-if-you-like-being-informed-b5e1968173684dfd908f4a85c91ef6e7"

At this point it would nice to be able to test these commands and make sure everything is working. To do this you will need to open a terminal and navigate to the folder you ran you `yo hubot` command inside. Run the command `bin/hubot` to run a test bot to check your code. You should see something like this. Don't worry about the errors, they will not affect what we are doing.

    body-parser deprecated undefined extended: provide extended option node_modules/hubot/src/robot.js:447:21
    hubotblog> [Tue Mar 26 2019 16:29:57 GMT-0700 (Mountain Standard Time)] WARNING Loading scripts from hubot-scripts.json is deprecated and will be removed in 3.0 (https://github.com/github/hubot-scripts/issues/1113) in favor of packages for each script.

    Your hubot-scripts.json is empty, so you just need to remove it.
    [Tue Mar 26 2019 16:29:57 GMT-0700 (Mountain Standard Time)] INFO hubot-redis-brain: Using default redis on localhost:6379
    [Tue Mar 26 2019 16:29:57 GMT-0700 (Mountain Standard Time)] ERROR hubot-heroku-keepalive included, but missing HUBOT_HEROKU_KEEPALIVE_URL. `heroku config:set HUBOT_HEROKU_KEEPALIVE_URL=$(heroku apps:info -s | grep web.url | cut -d= -f2)`

    hubotblog>

Now we have hubot terminal we can use. Lets say "Hello."

    hubotblog> Hello
    hubotblog> Hello World

Great! Our bot has responded to us. Lets try our keyword command.

    hubotblog> !new members
    hubotblog> https://www.notion.so/dstarling/Click-me-if-you-like-being-informed-b5e1968173684dfd908f4a85c91ef6e7

Now we want to make sure someone can find these commands, lets test our help command. Notice I am using "hubotblog help" this is the name I used when creating my bot, you will need to refer to your bot with the name you used. If you are not sure, you can find your bot's name in your `package.json` file.

    hubotblog> hubotblog help
    hubotblog> hubotblog !new members - link to procedure for new members.
    hubotblog adapter - Reply with the adapter
    hubotblog animate me <query> - The same thing as `image me`, except adds a few parameters to try to return an animated GIF instead.
    hubotblog echo <text> - Reply back with <text>
    hubotblog hello - Say hello!
    hubotblog help - Displays all of the help commands that this bot knows about.
    hubotblog help <query> - Displays all help commands that match <query>.
    hubotblog image me <query> - The Original. Queries Google Images for <query> and returns a random top result.
    hubotblog map me <query> - Returns a map view of the area returned by `query`.
    hubotblog mustache me <url|query> - Adds a mustache to the specified URL or query result.
    hubotblog ping - Reply with pong
    hubotblog pug bomb N - get N pugs
    hubotblog pug me - Receive a pug
    hubotblog the rules - Make sure hubot still knows the rules.
    hubotblog time - Reply with current time
    hubotblog translate me <phrase> - Searches for a translation for the <phrase> and then prints that bad boy out.
    hubotblog translate me from <source> into <target> <phrase> - Translates <phrase> from <source> into <target>. Both <source> and <target> are optional
    ship it - Display a motivation squirrel

You will see we have our new functions returned here with the help command. What you may not have expected is all the other stuff. Most of these are external-scripts that are included with hubot. We will go over those later in this article. What is important is we have built two commands that work and are documented with our help command.

Next we will need to construct our welcome function to do this we will need to learn a few new things. Lets look at an example from the `example.coffee` file.

    enterReplies = ['Hi', 'Target Acquired', 'Firing', 'Hello friend.', 'Gotcha', 'I see you']
    leaveReplies = ['Are you still there?', 'Target lost', 'Searching']

    robot.enter (res) ->
    	res.send res.random enterReplies
    robot.leave (res) ->
    	  res.send res.random leaveReplies


The first thing you may notice is that we have an array for `enterReplies` and `leaveReplies` . We can use these to hold text that we will later use. Next you will notice we see `robot.enter` instead of `robot.hear` , what this is doing is waiting for someone to join a channel to trigger the robots response. So in this example when someone enters a channel the bot will evoke a response from the `enterReplies` array. We will be using a very similar function to create our welcome message.

To begin we will create a new file named `welcome.coffee` inside our scripts folder. We will start by creating our description.

    # Description:
    #   To welcome new members to the community
    #
    # Dependencies:
    #   None
    #
    # Configuration:
    #   None
    #
    # Commands:

Next lets construct our welcome message.

    module.exports = (robot) ->
    	robot.enter (res) ->
    		res.reply "Hello and welcome"

Here we see a something new `res.reply`. This is like `res.send` but it replies to the person that triggered the event. We will be using this to help us make this a private message directly to the user that triggers the event.

 To test this behavior it will be best to create our own slack workspace to test our bot out. You will need to start by going to [https://slack.com/](https://slack.com/) and creating a new workspace. Once you have a workspace you can go into your administration settings, and search the app directory for hubot. This will allow you get generate an api key for your slack to use with your hubot. You can find an in-depth guide for this process here [https://slack.dev/hubot-slack/](https://slack.dev/hubot-slack/).

One we have the api key we can pass it to our bot. We do this in our terminal while starting the bot. `HUBOT_SLACK_TOKEN=PASTE_YOUR_SLACK_TOKEN_HERE ./bin/hubot --adapter slack`

You should see your bot come online in your slack workspace, try messaging it and say "hello" you should see a reply of "Hello World." Lets try our enter command. Create a channel name onboarding and use `/invite @botname` . This will add the bot to the channel. Now you can leave the channel and rejoin. If everything is working you should be greeted with "Hello and Welcome". Great! We are almost there.

Next we will need to isolate this message to only be triggered in the onboarding channel, and turn the message into a private direct message. To do this we will need the room id. This is a code assigned to every slack channel. You can find it on your url. Navigate to the channel you want the bot in and look at your url. It will look similar to this. [`https://dstarlingdevelopment.slack.com/messages/CGMQQ9GSG/`](https://dstarlingdevelopment.slack.com/messages/CGMQQ9GSG/). What we need is the code between the last slashes `CGMQQ9GSG`. We will add this to to our [`welcome.coffee`](http://welcome.coffee) file to isolate this trigger to the #onboarding channel.

    module.exports = (robot) ->
      conversationId = "CGMQQ9GSG"
      robot.enter (res) ->
        if res.message.room == conversationId
          enterReply = "This is a private onboarding message."
          room = robot.adapter.client.rtm.dataStore.getDMByName res.message.user.name
          robot.messageRoom room.id, enterReply

Lets break this new function down so we can understand all the new parts. We added the `conversationId` which is just the id of the channel we want this command confined to. Then add an *if* conditional to the *robot.enter* statement.

 We have also moved the reply into a variable to make the code a bit more clean. Next we have defined the room. With hubot you can think of a room as the channel as message takes place in. It's important to note that private messages also have a room.id even though it is a private message. `robot.adapter.client.rtm.dataStore.getDMByName` this is from the slack api and allows us to create a room with the the bot and user in it.

Once we have that we can use `robot.messageRoom room.id` to open a direct private message and then enter our reply with `enterReply`. Restart your bot in the terminal and test it out. If you join your #onboarding channel and get a direct message from your bot everything is working.

You should be able to reply to this message with the "help" command to see a full list of commands. Some of these may look unfamiliar, but they come from some external scripts that are included with the hubot bundle.

## External Scripts

External scripts are simply scripts written by other people people and published to the npm registry. Some are very complex and powerful, other are simple, fun, or silly. Most of these are very easy to get started. You can find the most complete list of these here [https://www.npmjs.com/search?q=hubot](https://www.npmjs.com/search?q=hubot). If you open your `external-scripts.json` file you should see something like this.

    [
      "hubot-diagnostics",
      "hubot-help",
      "hubot-heroku-keepalive",
      "hubot-google-images",
      "hubot-google-translate",
      "hubot-pugme",
      "hubot-maps",
      "hubot-redis-brain",
      "hubot-rules",
      "hubot-shipit"
    ]

These are all the external scripts that are bundled with hubot. Lets try one of them out real quick. We are going to test the `hubot-pugme` script. You can find information on it here [https://www.npmjs.com/package/hubot-pugme](https://www.npmjs.com/package/hubot-pugme). If we activate our test environment and type `hubot pug me` we should see a link returned. Remember to replace `hubot` with the name of your bot. This is how easy many external scripts are to setup. Browse the npm registry to find a package that suits your needs then:

---

- `npm i package-name-here`

- Add the script name to the `external-scripts.json` file.

    [
      "hubot-pugme"
    ]

- Read the documentation to learn the keywords and and additional setup that is required for more complex scripts.

---

Get started by exploring the included scripts by default and once you are comfortable you can start adding your own.

## Deployment

To deploy your bot, you will need a Heroku account. There are other options, but Heroku is very easy to get running with a few simple commands, and has a free tier. Once you have a heroku account, install the CLI tools found here: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli). If you have homebrew you can use `brew tap heroku/brew && brew install heroku` .

Once this is installed you will  be able to open a terminal in your root project directory and type `heroku login` . This will take you through a login process to use the CLI tools.

Once this is complete you will need git in your project. Use `git init` then you can `git add .` and `git commit -m "initial commit"` . You will need to create a repo on github for the bot then you can use `git remote add origin [https://github.com/Dstar4/example.git](https://github.com/Dstar4/example.git)` to set this as the project repository. From here you can `git push origin master` .

Next we will want to push our project to Heroku. To do this we will need to set our api key for slack into our Heroku config.

First we will create our Heroku project with `heroku create` . Then `heroku config:set HUBOT_SLACK_TOKEN=PASTE_YOUR_SLACK_TOKEN_HERE` . At this point everything should be ready, use `git push heroku master` to deploy your bot. At this point if everything went right you should see your bot come online in your slack  channel.

If you encounter problems, make sure to look at the heroku logs with `heroku logs` , this will give you a better idea what is wrong.

This is a good resource for deployment as well [https://hubot.github.com/docs/deploying/heroku/](https://hubot.github.com/docs/deploying/heroku/)

From here you have the skills you need to continue improving your bot and your community as a byproduct of that. Deployment can be tough, but just remember to read the logs and google the errors if you need to.

You can find the full repo for this project here: [https://github.com/Dstar4/hubotBlog](https://github.com/Dstar4/hubotBlog)

If you run into trouble you can find me on twitter [https://twitter.com/Dstar3248](https://twitter.com/Dstar3248) Feel free to send me a message and I will try and help out. Thanks for reading and enjoy your bot creation!
