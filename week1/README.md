# Week 1 Tasks

## Task 1 — Extract frames from a YouTube video
- Downloaded a YouTube video using `yt-dlp`
- Extracted sample frames using `ffmpeg`
- **Output:** `output_frame_001.jpg`, `output_frame_008.jpg`, `output_frame_020.jpg`

## Task 2 — Extract 1800 frames & rebuild video
- Extracted 1800 frames (30 fps × 60 seconds) from a 1-minute portion of the video using `ffmpeg`
- Re-stitched the frames back into a 1-minute video at 30 fps using `ffmpeg`
- **Input video:** `input_task2.mp4`
- **Rebuilt video:** `output_task2.mp4`

## Task 3 — Add audio track
- Downloaded a 1-minute music track from Pixabay
- Clipped audio to match video duration
- Merged audio with the video from Task 2 using `ffmpeg`
- **Final output:** `final_task3.mp4`

## Files
| File | Description |
|------|-------------|
| `video.mp4` | Original downloaded YouTube video |
| `input_task2.mp4` | 1-minute portion used for Task 2 |
| `output_task2.mp4` | Video rebuilt from 1800 frames |
| `final_task3.mp4` | Final video with audio merged |
| `audio.mp3` | Music track from Pixabay |
| `output_frame_*.jpg` | Sample extracted frames |
| `notes.txt` | Original task instructions |
