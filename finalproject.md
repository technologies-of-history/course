---
layout: page
title: Final Podcast
---

In lieu of a final exam, students will produce an 8- to 10-minute podcast about one of the communications revolutions we’ve discussed over the course of the semester, *excluding our unit on social media*. Your podcast should convince listeners why the technology you’ve chosen is the most significant communications revolution in history by comparing it with at least three other technologies discussed in this course. Finally, your podcast will reflect on how your chosen revolution is or is not similar to the ongoing revolution in digital communications technologies through which we’re all living. 

**Technologies to choose from include:**

- The invention of writing/the alphabet
- The widespread use of public, commemorative writing in the ancient world
- The invention of the codex in relation to the religions of the book
- The invention and widespread adoption of paper for bureaucratic/administrative writing
- The emergence of the how-to book and its influence on medicine and science
- The invention of the printing press
- The role of map-making and new cartographical technologies in the advancement of global exploration
- The invention of the public postal service and the role of correspondence in the Scientific Revolution/Enlightenment
- The emergence of the newspaper and its role in the Age of Revolutions
- The role of mass media (radio) in the politics of the early twentieth century

To receive full credit, you must discuss **at least three** of the readings assigned this semester, and **at least one** of the digital archives, projects, or repositories we've worked with this semester. You should compose a clear, evidence-based, and historically-grounded argument as to why you believe your chosen technology was the most significant. A successful podcast will also be convincing! 

Full instructions for how to create and submit the podcast are below. Your final podcast is **due on GitHub by 11:59 pm on Monday, May 4**. We will listen to one another's podcast episodes and celebrate the end of the semester during our assigned exam time, on Tuesday, May 5, from 11:00 am to 1:30 pm. Lunch will be provided!

## Step 1: Draft your podcast

1. **Before class on Tuesday, April 27**, you should draft an outline of your podcast. In this outline, you will identify which of the three communications technologies you'll compare with your chosen "revolution," as well as the secondary sources you plan to cite. You will draft an intro and conclusion for peer review in class on that day.
2. After receiving feedback from your peers and prior to recording your podcast, you will draft a script to ensure that your podcast falls within the 10-minute limit. In my experience, one double-spaced typed page takes around 2 minutes to read out loud. So plan accordingly.


## Step 2: Record and edit your podcast

1. Because this podcast is not intended for widespread distribution on public sites, I will not ask you to rent equipment or book time in a recording studio to produce a professional-quality podcast (as I do for students producing a season of the [FrogCast](https://frogcast.tcu.edu/season-5/)). The best way to get a quality recording at home is to sit in a quiet room without lots of hard surfaces (a closet works nicely) and use your phone's microphone to record. If you have a professional microphone, by all means use that!
2. If you use an iPhone and a Mac, you can even use your phone's microphone remotely to record in Audacity. When you open the program, simply click the **Audio Setup** button in the top menu, scroll to **Recording Device** and select your iPhone.
3. Even if you can't link your phone to Audacity's interface, you can use your phone to record segments of audio that you can then upload into Audacity to edit. To do so, export your audio files from your phone to your computer. Then, in **Audacity**, open the **File** menu in the top bar, then click **Import**, select **Audio** and locate the files saved on your computer.
4. Using Audacity's editing tools, remove background noises and adjust audio levels. Add sound effects and background music as you wish!
5. When you've finished, export your completed podcast as an .mp3 file and save it somewhere on your computer.

## Step 3: Upload your audio file
1. Within the [spring-2026-data](https://github.com/technologies-of-history/spring-2026-data) repository in our course GitHub organization, navigate to the **audio** folder.
2. Click **Add file** and then select **Upload files**.
3. Drag and drop your completed podcast (saved as an .mp3 file) into the folder and **Commit** your changes.

## Step 4: Draft your post
1. Create a new branch in our **spring-2026** repository called **lastname-final**. Within your branch, navigate to the **_posts** folder, and create a new Markdown file with the appropriate filename (YYYY-MM-DD-Your Title.md). Be sure to include the appropriate YAML header at the top of your Markdown file.
2. Begin your post with a few lines introducing your podcast and include **at least one image** of the technology you've chosen for your podcast.
3. Next, copy-and-paste the following lines of code into your post:
 
```
<html>
<div class="custom-audio-player">
  <h4 class="audio-title">Your Title Here</h4>
  <h5 class="audio-description">A brief description of the episode here. One sentence!</h5>
  
  <audio controls>
    <source src="https://technologies-of-history.github.io/spring-2026-data/audio/yourfilename.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
</div>
</html>
```

4. Update the title of your episode from `Your Title Here` to whatever you want to call your episode. Beneath the title, where you see `A brief description...`, go ahead and add a sentence describing your episode. Finally, update the url within the `<source>` tag with your filename.
5. Beneath this bit of code, add a section in your post called **Sources Cited** and include your bibliography here. Please include links (which you can copy from our course syllabus site) where applicable. You should link to any secondary sources *or* digital projects that you mention in the podcast. 

## Step 5: Submission

Create a pull request by 11:59 pm on Monday, May 4, and you're done! We'll listen to everyone's episodes the following day in class!