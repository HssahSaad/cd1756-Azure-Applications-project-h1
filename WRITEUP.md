# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

For deploying the CMS app, I decided to go with Azure App Service. It just made the most sense for the size and needs of this project.

First, it handles most of the background tasks like scaling, monitoring, and applying updates without me having to worry about them. That was a big plus since I wanted to focus on building the app, not managing servers.

Second, it integrates smoothly with GitHub Actions, so every time I push changes to the main branch, the app gets updated automatically. That made continuous deployment super simple.

Another reason is cost. App Service is more affordable and easier to manage than setting up a full VM, especially for a small-to-medium web app like this one.

Lastly, App Service already supports Python, logging, and environment variables out of the box. I didn’t have to do any extra configuration to get things working.


### Assess app changes that would change your decision.
If this app grows in the future or starts needing more advanced features, I might have to rethink this setup.

For example, if I ever need to install system-level tools or make OS-level changes that App Service doesn’t support, I’d consider switching to a Virtual Machine.

Also, if the app starts handling more demanding tasks—like processing videos, running background jobs, or dealing with high-performance workloads—a VM would give me more control and better performance.

Another case is if I want to host multiple services or containers that need to work closely together. Managing those on a single VM could be easier than separating them in App Service.

But for now, App Service strikes the right balance between simplicity, cost, and functionality. It’s exactly what I needed for this stage of the project.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
