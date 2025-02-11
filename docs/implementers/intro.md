This implementation guide is divided in 3 sections which correspond to the typical implementer approach:

## 1. Evaluate
For those new to Ozone, this section outlines various assessment options. It includes:

- A link to the online demo
- Instructions for running Ozone locally
- Guidance on using Ozone within a Gitpod environment

## 2. Adopt
Once you've determined Ozone's suitability for your project, it's time to set up your environment.
First and foremost, you will want to create your own copy of Ozone (aka, distribution), so that you can configure it or customize it to your needs. This is essential to adopt Ozone. We have developed a comprehensive tool suite to facilitate implementers creating their own distribution. Such distribution will be at first, an empty shell that will just inherit a plain Ozone. Progressively, you will be able make it your own, but under the hood still depending on the most recent version of Ozone, directly benefiting from its new features and fixes.

## 3. Deploy
Finally, once your software is ready and packaged, you can deploy it to your server. Ozone provides some utils scripts to help you with this. Additionally, it comes with backup and restore functionality as well as monitoring. We also provide in that section a page for common errors and troubleshooting tips.

