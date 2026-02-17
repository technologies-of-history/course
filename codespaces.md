--- 
layout: page
title: How to check your work in GitHub CodeSpaces
---

## Step 1: Open a Virtual CodeSpace

While in your **lastname** branch in **technologies-of-history/spring-2026**, click the green **Code** button at the top right. Select **CodeSpaces** and then click **Create codespace on [yourbranch]**. A new browser window will open that mimics the interface of Microsoft VS Code, the text editor that integrates with GitHub.

On the far left of the page, you'll see a vertical menu that contains six icons, but you only need to worry about the top three: a file symbol; a magnifying glass; a network icon.

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespace1.jpg){:width="300px" .center-image}

Click the **file icon** at the top of this vertical menu, and you'll see the file structure of your branch of the **spring-2026** repository. If you click the **_posts** folder, you'll see your draft of the post for this digital tools assignment. Click on that Markdown file, and you'll see all of your code.

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespaces2.jpg){:width="300px" .center-image}

To check to see if you did everything correctly, we're going to bring up the **virtual terminal** to use the **command line**. At the top right, you'll see a series of boxes with dividers, which dictate which menus are showing in your VS Code interface. 

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespaces3.jpg){:width="800px" .center-image}

If it isn't already selected, click the box divided horizontally down the middle to bring up your terminal. You'll see a new interface appear at the bottom of your browser window with a line of text that reads like this:
`@yourusername -> /workspaces/spring-2026 (lastname-dt2) $` This line tells you that your terminal is open in the **spring-2026** repository and in your **lastname-dt2** branch, so any commands you execute will be performed in this repository and on this branch. This is what we want! Type the command `jekyll serve` after the dollar sign and hit enter.

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespaces4.jpg){:width="800px" .center-image}

 You'll get some warnings about deprecated sass (ignore these), but note the **pop-up window** that appears at the bottom right of your browser window. Click **Open in browser**, and you've now been taken you to a url that loads our course blog on locally on your machine.

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespaces5.jpg){:width="800px" .center-image}

You may see the 404 page at first, and that's fine. Click the site title and you'll end up on our homepage, where you should see your draft blog post as the top item in the blogroll. Click the title of your post to open the full page and check to see that it looks the way you want it to.

![Screenshot of virtual VS Code in GitHub Codespaces]( {{ site.baseurl }}/assets/images/codespaces6.jpg){:width="800px" .center-image}

If it doesn't look the way you want it to, return to the CodeSpace you've got open in another tab. See if you can identify the problem. Tweak your code, then hit **Command+S** (for Mac users) or **Conrtol+S** (Windows users). The server will automatically refresh the site build. You'll just navigate back over the tab where you were viewing the post and click refresh to see your changes appear on the page.

9. Once you're happy with how your post looks, you'll need **Commit** any changes you made to your code. Return to the Codespace that's open in your browswer tab and click the **Network** icon at the far left vertical menu. This will bring up a list of all the files that have changed since you opened the repository. You'll see lots of files with names that just look like strings of numbers; these are the temporary files generated to build the site, and you should **ignore** those. 
10. Scroll down until you find the filename of your blog post, **YYYY-MM-DD-Your title..md**. Right click that filename and select **Stage changes**. Once you do, you'll see that file move above all the others, underneath a box for you to type in your **Commit message**. Type in your message, and click **Commit.**
11. Finally, tell the Jekyll site builder to stop serving your site by clicking somewhere in the terminal window at the bottom of your Codespaces window (the cursor should go solid blue when you do) and typing **Control+C**. Jekyll will stop serving your site now. You can close the Codespaces browswer window and the browswer window you were using to view your blog post. Your very last step is to click the green **Code** button at the top of our **spring-2026** repository and select **Codespaces** if it's not already open. Click the three dots to the right and select **Delete codespace.**