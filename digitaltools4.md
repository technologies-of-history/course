---
layout: page
title: Digital Tools 4
permalink: /digitaltools4
---

# Mapping History

You’ve already embedded an interactive map in your second Digital Tools assignment. Now, for your fourth Digital Tools Assignment, you will use a more robust mapping tool to create a visual and spatial historical narrative. [ArcGIS Online](http://tcugis.maps.arcgis.com) is an online interface for creating Geographical Information Systems (GIS). GIS is a means of connecting data to a map, integrating location data (where things are) with all types of descriptive information (what things are like there). It does so by presenting data as layers that can be visualized on a base map. For this assignment, you'll create one of those layers by georeferencing an early printed map from [Old Maps Online](https://www.oldmapsonline.org/) to present geospatial data on a singular voyage of discovery (gathered from the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site) by creating and sharing your own ArcGIS Story Map.

## Step 1: Choose a Voyage Dataset & Find a Historical Map

1. Select a dataset of voyage coordinates and dates relating to one early modern voyage (between 1450 and 1800) from the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site. You'll select your dataset from the **.csv** file that appears when you click **Dowload Data** at the top right of the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site.
2. Right click the webpage and click **Save As...**. Save the file somewhere on your computer, making sure you add **.csv** to the end of the filename.
3. Double check that you've created the file correctly by opening the **.csv** file you created (in Excel or Google sheets). Once the file is open, you can delete all the data you **don't** need, keeping only the coordinates and dates for your chosen voyage.
4. Now that your dataset is selcted, visit [Old Maps Online](https://www.oldmapsonline.org/) to find a historical map that matches the region and era of your voyage. For example, if you've selected Captain Cook's first voyage, you might want to find a map of Polynesia and Australia from the early 1800s.
5. You can find a map that fits the bill by using the bottom timeline slider to adjust the era of map you're looking for, and then changing the map view to focus on the area of the globe you'd like to see maps for. Make sure the map you choose is from the **David Rumsey Collection** (you can tell because you'll see the black box with the David Rumsey logo next to the map image.)
6. After finding a map to work with in [Open Maps Online](https://www.oldmapsonline.org/), navigate to [David Rumsey Map Collection](https://www.davidrumsey.com) and copy-and-paste the title of the map you've selected into the search box. You'll be able to see the full title of your chosen map if you click the **Document** button at the far right of the menu directly above the map.
7. Once you've located your map on the [David Rumsey Map Collection](https://www.davidrumsey.com), click **Export** at the top right and select **Extra Large**. You'll get a folder with a **.jpg** file and a **.txt** file. You don't need the **.txt** file, but save the **.jpg** file somewhere you'll remember on your computer.

## Step 2: Georeference your chosen map with ArcGIS

1. Log into [ArcGIS Online](http://tcugis.maps.arcgis.com) and click **Map** in the top menu.
2. Click the **plus sign** at the top left and select **Add Media Layer.** Drop and drop the downloaded **.jpg** file of your chosen historical map into the box.
3. Once your image loads, your historical map will appear over the base layer world map. You now have the opportunity to align it with the base map, roughly georeferencing it for future use.
4. You'll have the option to move the image around, resize it, and even rotate it, if necessary. You can play with the transparency slider so you can see both the historical map and base layer to line them up.
5. Once you get the map roughly where you want it, at the bottom left, click **Side-by-Side** to create a set of georeferenced points. Essentially, you'll place each of the four points in exactly the same spot on both maps. This will warp the map to more accurately create a georeferenced layer.
6. Save the map you've created to your account.

## Step 3: Create your Story Map with ArcGIS
1. Visit [storymaps.arcgis.com](https://storymaps.arcgis.com) and log in using your username and password for ArcGIS. 
2. Create a new Story Map, titling it whatever seems best for your particular voyage of exploration. Click the plus sign to add an element and scroll down to select **Map Tour**. Select **Start from Scratch** and then select a **Map Focused Guided Tour**, the option on the top left.
3. Click the pencil icon in the map section of your StoryMap. When the new map menu opens, click the box under **Select basemap** and select **Browse more maps**. This should bring you to a page with your saved content, where you can select your saved georeferenced historical map.
4. Now you can create a StoryMap with the coordinates of your selected voyage of exploration. Each coordinate should be one a slide in the story. You'll add a location for a each slide, and upload a photo (use your imagination) and a brief decription of that stage of your chosen voyage.
5. Once you're finished with your StoryMap, you'll need to **Publish** it so that it can be embedded in your post. Be sure to select **Public** from the dropdown menu, but you can deselct "Allow duplication" and "Show in Web Search Results."
6. Once your StoryMap is published, open up your StoryMap to view it, and click the three dots in the topbat menu at the far right. Select **Embed this story** and then copy the code that appears.

## Step 4: Compose your post
1. Create a Markdown file according to our course protocols (fork or open the **spring-2026** repository in your personal account, locate the **_posts** folder, and create or upload a file named **YYY-MM-DD-Your Title.md.**)
2. Compose a 4-5 paragraph post responding to the following question:
- What boyage of exploration did you choose and why?
- How does your historical map reflect the scope of geographic knowledge, navigational skill, and cartographic expertise at the time of your chosen voyage?
- How did your particular voyage of exploration transform the way the world was understood and depicted at the time?
- In your opinion, have digital tools for map-making and geocoding, captured in Geographic Information Systems, transformed the way we understand visualize and understand human interaction with the physical world in the same ways as 'tracks on the ocean' as described by Sara Caputo?
3. Decide where you'd like your StoryMap to appear in your post, and then paste the embed code you copied from ArcGIS online, making sure to wrap the code in `<html>` tags.

## Step 5: Submit your post
Commit your changes and submit a pull request to **technologies-of-history/spring-2026**, and you're done!
