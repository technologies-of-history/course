---
layout: page
title: Digital Tools Assignment 1
---
## Communicating Simply

By now you've created a [GitHub](https://github.com) account, practiced opening a repository, making changes to a file, making a pull request, and merging branches with GitHub's [Hello World](https://guides.github.com/activities/hello-world/) tutorial. You've followed the [Markdown lesson](https://programminghistorian.org/en/lessons/getting-started-with-markdown) on the Programming Historian, so you know how to style your text files with Markdown syntax. We've practiced authoring Markdown files in class, but now it's time to do it on your own and create content for our course blog. You'll be following these same steps to create and submit the rest of your Digital Tools assignments, so it's very important for you to get the hang of these basic steps now.

## Step 1: Think about downloading a text editor

All of your digital assignments this semester will be authored in Markdown, which means 
you can't use Google Docs or Microsoft word to create them. As you know, you can always 
create Markdown files (.md) directly in GitHub, but if you'd like to be able to complete 
your assignments offline, save your work on your own machine, and preview your work in a 
local development environment on the developer, then you will want to use a text editing program to write and save your .md files. If you've done some programming/coding 
before, you likely already have a favorite text editor, and you should keep using it. If not, I really like [Visual Studio Code](https://code.visualstudio.com/) which can run on MacOS, Windows, or Linux and integrates directly with GitHUb. It's become the standard text editor in the field as it incorporates GitHub's AI help for coding.

## Step 2: Take a look at an existing post

1. Open the **spring-2026** repository in our course GitHub organization. 
2. Find the **_posts** folder and open it. 
3. You'll see a single file in there titled **2024-11-04-Welcome to our course.md**. This is the Markdown file for the blog post that appears on the homepage of our course website. 
4. Note the file naming conventions. All of the blog posts created for our site must be named in the same way: **yyyy-mm-dd-your title.md**.
5. Click on the **2025-12-07-Welcome to Technologies of History.md** file in your GitHub repository, and then click on the pencil icon in the upper right to edit the file. You should now see the post written in Markdown with a header at the top that looks like this:

 ```
 ----
layout: post
author: Melissa Reynolds
title: Welcome to Technologies of History
excerpt_separator: <!--more-->
---
 ```

6. Note the formatting of this file. The heading at the top is very important, and every post you write to submit a Digital Tools Assignment must contain these items:
- `layout: post` tells the Jekyll developer to use the layout to style the Markdown that follows. Other **.md files** that you see in the **spring-2026** repository, but not in the **_posts** folder, are set to `layout: page`, which tells the developer to use a different style for the Markdown that follows.
- `author: Melissa Reynolds` tells the Jekyll site builder to publish this name as author in the subheader of the post. It also tells the Jekyll site builder that this post should be linked under the author Melissa Reynolds in the **Contributors** page. 
- `title: Your title here` is pretty self explanatory. This is the heading that will appear at the top of your post. You should type whatever title you'd like for your post after the colon.
- `excerpt_separator: <!--more-->`: This tells the Jekyll builder how much of the post to preview on the blog feed. When you draft your post, include this snippet of code `<!--more-->` just beneath the first or second paragraph of text in the post, and Jekyll will know to publish only the text above that code and to include a **READ MORE** link at that point on the blog's homepage.


## Step 3: Create a new Markdown file in which to compose your assignment

(Note: the following instructions are for those of you brand new to GitHub, who don't use a text editor. This is the *most basic* way to add a file to your repository, but if you already know how to create a branch, push changes and commit, and initiate a pull request via those other platforms, go right ahead.)

__If you're working directly in GitHub:__
1. Navigate into the **spring-2026** repository in our GitHub organization.
2. Create a new branch in the **spring-2026** repository by clicking the arrow to the right of **master** in the branch menu. In the text box that appears, type in the name of the new branch you'll create using the following naming convention: **lastname-dt1**.
3. Below that text box, click the option that appears that says **Create branch: lastname-dt1**.
4. Within in this new branch, open the **_posts** folder. 
5. At the top right, click **Add New File** and select **Create New File** to open GitHub's text editor.
6. Name this new file according to the following naming conventions: **yyyy-mm-dd-your title.md**. ALL posts you create for this course blog must follow these exact naming conventions.
7. Create your YAML header following these conventions:

 ```
 ----
layout: post
author: Your Name Here
title: Your Title Here
excerpt_separator: <!--more-->
---
 ```

__If you're writing your posts in a text editor rather than on GitHub:__
1. Open your text editor of choice and create a new create a new Markdown file with the appropriate naming conventions: **yyyy-mm-dd-your title.md**. 
2. Create your YAML header as specified above and continue to **Step 4** below.
3. When you've finished drafting your post, follow create a new branch in the **spring-2026** repository as described above, but instead of clicking **Create New File** within the **_posts** folder in your new branch, you'll click **Upload files** to add your post to the repository.

## Step 4: Write your post

Using appropriate Markdown syntax, Write a 2–3 paragraph post reflecting on the relationship between the
nature or format of a communication technology and the kind of knowledge that technology can
produce. Historians have suggested, for example, that alphabetic writing enabled 
the development of philosophical thought in Greece that was markedly different from that of ancient
Mesopotamia, with its cuneiform syllabary. In what ways do we see a similar relationship between
the principles of static computing and the production of digital scholarship? Are historians
arguments constrained or shaped by the digital tools available to them? How might the digital environment transform historians' scholarship?

To receive full credit for this assignment, be sure to draw comparisons between the arguments expressed by Goody and Van De Mieroop in their respective articles and those you develop related to digital communications. Use parenthetical citations (lastname page#) to cite these works if necessary.

## Step 5: Commit your post

1. After you create (or upload) your Markdown file, you'll need to **Commit changes...** to save the file to your branch (the green button on the upper right).
2. If you're composing your post online in GitHub's web interface, every time you make a change in the file, you'll write up a brief description of what you changed (the **Commit message**) and click, **Commit** to save. Be sure to select the option to commit to **your** new branch, **lastname-dt1**.
3. If you're composing your post on the GitHub web interace, you'll **Commit changes...** every time you make a change to the file. You can work on it over several days as long as you **commit** every time before you close out of the interfact. If you draft your post in a text editor, you'll only **Commit Changes...** once, after you upload the file.
4. Git stores each of the versions of your file at every **Commit**, making it possible to revert back to a previous version of the file at any time. You simply click the **History** tab at the top right, and GitHub will show you a page with your entire commit history for that branch.
5. **Committing changes...** does NOT publish your post to our course site. You can continue working on your draft post as much as you like in your **lastname-dt1** branch, and nothing will get published until your submit a **Pull request.**

## Step 6: Submit a pull request

Once you're happy with your post and have committed your changes, you're ready to submit the assignment. It's time to notify the developer (me) that you'd like the post to be merged into the **master** branch of the site so that it can be served to the website. 

1. Be sure to check and make sure you're in your **lastname-dt1** branch.
2. In the menu at the top of the page, click **Pull requests**. 
3. Click the green button **New pull request**. 
4. You'll now see a gray box at the top that shows you the **base** repository you'll be sending your changes to and a drop-down menu to select the branch you want to **compare.** Select your branch **lastname-dt1** as the branch to compare, and be sure the **master** branch is the **base**.
5. Name your pull request **Digital Tools 1 Submission** and then click **Create pull request**.

Ok, that's it! You've written a blog post in Markdown and followed the standard GitHub workflow to send it to our class site. Pat yourself on the back, and know that you'll do it all over again for the next four assignments.
