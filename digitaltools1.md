---
layout: page
title: Digital Tools Assignment 1
permalink: /digitaltools1
---
## Communicating Simply

By now you've created a [GitHub](https://github.com) account, practiced opening a repository, making changes to a file, making a pull request, and merging branches. You've followed the [Markdown lesson](https://programminghistorian.org/en/lessons/getting-started-with-markdown) on the Programming Historian, so you know how to style your text files with Markdown syntax. We've practiced authoring Markdown files in class, but now it's time to do it on your own and create content for our course blog. You'll be following these same steps to create and submit the rest of your Digital Tools assignments, so it's very important for you to get the hang of these basic steps now.

### Step 1: Think about downloading a text editor

All of your digital assignments this semester will be authored in Markdown. As you know, you can always 
create Markdown files (.md) directly in GitHub or Google docs, but if you'd like to be able to complete 
your assignments offline, save your work on your own machine, and preview your work in a 
local development environment, then you will want to use a text editing program to write and save your .md files. If you've done some programming/coding before, you likely already have a favorite text editor, and you should keep using it. If not, I really like [Visual Studio Code](https://code.visualstudio.com/) which can run on MacOS, Windows, or Linux and integrates directly with GitHUb. It's become the standard text editor in the field as it incorporates GitHub's AI help for coding. 

**Note:** *If you'd like to check your work by serving your branch of our site locally, you'd need to install [Jekyll](https://jekyllrb.com/docs/installation/) on your computer. The process can be tricky, depending on your operating system, and it requires knowledge of the command line. You'd also need to have Ruby and Ruby gems installed, which is where most of the headaches emerge. BUT! If you're an experienced coder, I'm happy to help you install Jekyll. Send me an email or come talk in office hours.*

### Step 2: Take a look at an existing post

1. Open (or Fork) the **spring-2026** repository in **your** GitHub account. [NB: You'll know you're in **your** personal repository if you see your user name at the top left and not technologies-of-history.] 
2. Find the **_posts** folder and open it. 
3. You'll see a single file in there titled **2024-11-04-Welcome to our course.md**. This is the Markdown file for the blog post that appears on the homepage of our course website. 
4. Note the file naming conventions. All of the blog posts created for our site must be named in the same way: **yyyy-mm-dd-your title.md**.
5. Click on the **2025-12-07-Welcome to Technologies of History.md** file in your GitHub repository, and then click on the pencil icon in the upper right to edit the file. You should now see the post written in Markdown with a header at the top that looks like this:

 ```
 ----
layout: post
author: Melissa Reynolds
title: Welcome to Our Course
excerpt_separator: <!--more-->
---
 ```

6. Note the formatting of this file. The heading at the top is very important, and every post you write to submit a Digital Tools Assignment must contain these items:
- `layout: post` tells the Jekyll developer to use the layout to style the Markdown that follows. Other **.md files** that you see in the **spring-2026** repository, but not in the **_posts** folder, are set to `layout: page`, which tells the developer to use a different style for the Markdown that follows.
- `author: Melissa Reynolds` tells the Jekyll site builder to publish this name as author in the subheader of the post. It also tells the Jekyll site builder that this post should be linked under the author Melissa Reynolds in the **Contributors** page. 
- `title: Welcome to Our Course` is pretty self explanatory. This is the title of your post that will appear at very top, styled as `<h1>`. You should type whatever title you'd like for your post after the colon.
- `excerpt_separator: <!--more-->`: This tells the Jekyll builder how much of the post to preview on the blog feed. When you draft your post, include this snippet of code `<!--more-->` just beneath the first or second paragraph of text in the post, and Jekyll will know to publish only the text above that code and to include a **READ MORE** link at that point on the blog's homepage, which will link readers to your full post.


### Step 3: Creating a Markdown file

(Note: the following instructions are for those of you brand new to GitHub, who don't use a text editor. These are the *most basic* ways to add a file to your repository, but if you already know how to create a branch in your text editor, commit and push changes, and initiate a pull request via those other platforms, go right ahead.)

__If you're working directly in GitHub:__
1. Navigate into the **spring-2026** repository in your personal account, and then select the **_posts** folder. 
2. At the top right, click **Add New File** and select **Create New File** to open GitHub's text editor.
3. Name this new file according to the following naming conventions: **yyyy-mm-dd-your title.md**. ALL posts you create for this course blog must follow these exact naming conventions.
4. Create your YAML header as specified above and compose your post.

__If you're writing your posts in a text editor or on Google docs rather than on GitHub:__
1. Open your text editor or Google docs. 
2. Create your YAML header as specified above and compose your post following the directions in **Step 4**, below.
3. When you've finished drafting your post, download the file as a .md with the following naming convention: **yyyy-mm-dd-your title.md**
4. In your **spring-2026** repository, locate the **_posts** folder. Click **Add New File** at top right, and then select **Upload file**. Drag and drop your **.md** file and continue to **Step 5** below.

### Step 4: Compose your assignment using appropriate Markdown syntax 

Historians have suggested that alphabetic writing enabled the development of philosophical thought in Greece that was markedly different from that of ancient Mesopotamia, with its cuneiform syllabary. What does this argument suggest about the structure of a language and what that language makes possible? What are the implications of this argument for the way we think about computer languages?

To receive full credit for this assignment, be sure to draw comparisons between the arguments expressed by Goody and Van De Mieroop in their respective articles and those you develop related to digital communications. Use parenthetical citations (lastname page#) to cite these works if necessary.

Your post should include the following elements of Markdown code:
- At least one heading
- At least one link
- At least one image 

**Note:** *I've added a little extra CSS to our course site so you can style the images you embed by adding Liquid code immediately after the ordinary syntax for embedding an image. This brief snippet of [Liquid](https://shopify.github.io/liquid/basics/introduction/) enables you to size and position your image within your text block. Simply designate the width you'd like your image to be (in pixels), and then decide whether you want your image to appear wrapped in text on the right* `.right-image` *or left* `.left-image` *or all by itself in the center of your screen* `.center-image`. *An example of the correct code snippet for an image sized at 270 pixels and wrapped in text on the right, is as follows:*  
`![Image alt text](link to image url){:width="270px" .right-image}`

### Step 5: Commit your post

1. After you create (or upload) your Markdown file, you'll need to **Commit changes...** to save the file to your branch.
2. If you're composing your post online in GitHub's web interface, every time you make a change in the file, you'll write up a brief description of what you changed (the **Commit message**) and click, **Commit** to save. You'll be prompted to either **Commit changes** to a **new branch** or to the **master branch**, and to save yourself an extra step, just go ahead and choose the top option and commit to the **master branch** of your repository.
3. If you draft your post in a text editor or on Google docs, you'll only **Commit Changes...** once, after you upload the file. 
4. Git stores each of the versions of your file at every **Commit**, making it possible to revert back to a previous version of the file at any time. You simply click the **History** tab at the top right, and GitHub will show you a page with your entire commit history for that branch.
5. Remember, **Committing changes...** does NOT publish your post to our course site. You can continue working on your draft post as much as you like, and nothing will get published until you submit a **Pull request.**

### Step 6: Submit a pull request

Once you're happy with your post and have committed your changes, you're ready to submit the assignment. It's time to notify the developer (me) that you'd like the post to be merged into the **master** branch of course repository so that it can be served to the website. 

1. Be sure to check and make sure you're in your personal **spring-2026** repository (check the user name in the top left).
2. Then, in the menu at the top of the page, click **Pull requests**. 
3. Click the green button **New pull request**. 
4. You'll now see a gray box at the top that shows you the **base** repository you'll be sending your changes to [**technologies-of-history/master**] and the **head** branch you want to **compare** [**yourusername/spring-2026**].
5. Name your pull request **Digital Tools 1 Submission** and then click **Create pull request**.

Ok, that's it! You've written a blog post in Markdown and followed the standard GitHub workflow to send it to our class site. Pat yourself on the back, and know that you'll do it all over again for the next four assignments.
