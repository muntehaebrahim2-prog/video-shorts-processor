#!/usr/bin/env python3
"""
Standalone Video Generator for YouTube Shorts Processor
Generates sample test videos without needing the full processor setup
"""

import numpy as np
import imageio
from pathlib import Path
import sys
from datetime import datetime


def create_colorful_video(
    filename: str,
    duration: int = 10,
    fps: int = 30,
    width: int = 1080,
    height: int = 1920
):
    """
    Create a colorful gradient video with animation
    
    Args:
        filename: Output video filename
        duration: Video duration in seconds
        fps: Frames per second
        width: Video width (default 1080 for Shorts)
        height: Video height (default 1920 for Shorts)
    """
    print(f"🎬 Creating video: {filename}")
    print(f"   Duration: {duration}s | FPS: {fps} | Resolution: {width}x{height}")
    
    output_dir = Path("input_videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    
    num_frames = duration * fps
    frames = []
    
    print(f"   Generating {num_frames} frames...")
    
    for frame_idx in range(num_frames):
        # Progress
        if (frame_idx + 1) % (num_frames // 10) == 0 or frame_idx == 0:
            progress = (frame_idx / num_frames) * 100
            print(f"   Progress: {progress:.0f}%", end='\r')
        
        # Create frame
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Animated gradient background
        progress = frame_idx / num_frames
        
        # Create animated colors
        for y in range(height):
            # Vertical gradient
            r = int(128 + 127 * np.sin(progress * 2 * np.pi + y / height * 2 * np.pi))
            g = int(128 + 127 * np.sin(progress * 2 * np.pi + 2 + y / height * 2 * np.pi))
            b = int(128 + 127 * np.sin(progress * 2 * np.pi + 4 + y / height * 2 * np.pi))
            
            frame[y, :] = [r, g, b]
        
        # Add moving geometric shapes
        # Circle
        center_x = int(width * (0.5 + 0.3 * np.cos(progress * 2 * np.pi)))
        center_y = int(height * (0.3 + 0.2 * np.sin(progress * 2 * np.pi)))
        radius = 100
        
        y_grid, x_grid = np.ogrid[:height, :width]
        mask = (x_grid - center_x) ** 2 + (y_grid - center_y) ** 2 <= radius ** 2
        frame[mask] = [255, 100, 50]
        
        # Add text area (white rectangle at bottom)
        text_area_height = 200
        frame[-text_area_height:, :] = [50, 50, 50]
        
        frames.append(frame)
    
    print(f"   Progress: 100%")
    print(f"   Writing video file...")
    
    with imageio.get_writer(str(output_path), fps=fps) as writer:
        for frame in frames:
            writer.append_data(frame)
    
    file_size = output_path.stat().st_size / (1024 * 1024)
    print(f"✅ Created: {output_path}")
    print(f"   File size: {file_size:.2f} MB\n")
    
    return output_path


def create_gradient_video(
    filename: str,
    duration: int = 10,
    fps: int = 30,
    width: int = 1080,
    height: int = 1920,
    color_range: tuple = (50, 200)
):
    """
    Create a simple gradient video
    
    Args:
        filename: Output video filename
        duration: Video duration in seconds
        fps: Frames per second
        width: Video width
        height: Video height
        color_range: Tuple of (min_color, max_color)
    """
    print(f"🎬 Creating gradient video: {filename}")
    print(f"   Duration: {duration}s | FPS: {fps} | Resolution: {width}x{height}")
    
    output_dir = Path("input_videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    
    num_frames = duration * fps
    frames = []
    
    print(f"   Generating {num_frames} frames...")
    
    for frame_idx in range(num_frames):
        # Progress
        if (frame_idx + 1) % (num_frames // 10) == 0 or frame_idx == 0:
            progress = (frame_idx / num_frames) * 100
            print(f"   Progress: {progress:.0f}%", end='\r')
        
        # Create frame with gradient
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        progress = frame_idx / num_frames
        
        # Animate color
        base_color = int(color_range[0] + (color_range[1] - color_range[0]) * progress)
        
        for y in range(height):
            intensity = int(255 * (y / height))
            frame[y, :] = [base_color, intensity, 255 - intensity]
        
        frames.append(frame)
    
    print(f"   Progress: 100%")
    print(f"   Writing video file...")
    
    with imageio.get_writer(str(output_path), fps=fps) as writer:
        for frame in frames:
            writer.append_data(frame)
    
    file_size = output_path.stat().st_size / (1024 * 1024)
    print(f"✅ Created: {output_path}")
    print(f"   File size: {file_size:.2f} MB\n")
    
    return output_path


def create_text_overlay_video(
    filename: str,
    text: str = "YouTube Shorts",
    duration: int = 10,
    fps: int = 30,
    width: int = 1080,
    height: int = 1920
):
    """
    Create a video with text overlay
    
    Args:
        filename: Output video filename
        text: Text to display
        duration: Video duration in seconds
        fps: Frames per second
        width: Video width
        height: Video height
    """
    print(f"🎬 Creating text overlay video: {filename}")
    print(f"   Text: '{text}'")
    print(f"   Duration: {duration}s | FPS: {fps} | Resolution: {width}x{height}")
    
    output_dir = Path("input_videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    
    num_frames = duration * fps
    frames = []
    
    print(f"   Generating {num_frames} frames...")
    
    for frame_idx in range(num_frames):
        # Progress
        if (frame_idx + 1) % (num_frames // 10) == 0 or frame_idx == 0:
            progress = (frame_idx / num_frames) * 100
            print(f"   Progress: {progress:.0f}%", end='\r')
        
        # Create frame
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        progress = frame_idx / num_frames
        
        # Background with animation
        for y in range(height):
            hue = (progress * 360) % 360
            saturation = int(128 + 127 * np.sin(y / height * 2 * np.pi))
            frame[y, :] = [int(hue / 360 * 255), saturation, 200]
        
        # Add white text area in center
        text_y_start = height // 2 - 100
        text_y_end = height // 2 + 100
        frame[text_y_start:text_y_end, :] = [255, 255, 255]
        
        frames.append(frame)
    
    print(f"   Progress: 100%")
    print(f"   Writing video file...")
    
    with imageio.get_writer(str(output_path), fps=fps) as writer:
        for frame in frames:
            writer.append_data(frame)
    
    file_size = output_path.stat().st_size / (1024 * 1024)
    print(f"✅ Created: {output_path}")
    print(f"   File size: {file_size:.2f} MB\n")
    
    return output_path


def main():
    """Generate multiple sample videos"""
    print("\n" + "="*60)
    print("🎬 Video Shorts Processor - Video Generator")
    print("="*60 + "\n")
    
    print(f"⏰ Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        # Create different types of videos
        videos_created = []
        
        # 1. Colorful animated video
        print("📹 Video 1: Colorful Animated")
        print("-" * 60)
        videos_created.append(create_colorful_video("sample_video_1.mp4", duration=15, fps=30))
        
        # 2. Gradient video
        print("📹 Video 2: Blue Gradient")
        print("-" * 60)
        videos_created.append(create_gradient_video("sample_video_2.mp4", duration=12, fps=30, color_range=(50, 150)))
        
        # 3. Another gradient video
        print("📹 Video 3: Orange Gradient")
        print("-" * 60)
        videos_created.append(create_gradient_video("sample_video_3.mp4", duration=10, fps=30, color_range=(100, 200)))
        
        # 4. Text overlay video
        print("📹 Video 4: Text Overlay")
        print("-" * 60)
        videos_created.append(create_text_overlay_video("sample_video_4.mp4", text="YouTube Shorts", duration=8, fps=30))
        
        print("="*60)
        print(f"✅ SUCCESS: Generated {len(videos_created)} sample videos!")
        print("="*60)
        print(f"\n📁 Videos saved to: input_videos/\n")
        
        print("📋 Created videos:")
        for i, video_path in enumerate(videos_created, 1):
            file_size = video_path.stat().st_size / (1024 * 1024)
            print(f"   {i}. {video_path.name} ({file_size:.2f} MB)")
        
        print(f"\n⏰ End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n✨ Ready to process! Run:")
        print("   python examples/example2_batch_processing.py\n")
        
        return 0
        
    except ImportError as e:
        print(f"\n❌ Error: Missing required library")
        print(f"   {str(e)}")
        print(f"\n   Install with: pip install -r requirements.txt")
        return 1
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
