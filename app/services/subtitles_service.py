import os
import pysubs2

def save_as_txt(result: dict, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

def save_as_srt(result: dict, output_path: str):
    subs = pysubs2.SSAFile()
    for seg in result["segments"]:
        subs.append(pysubs2.SSAEvent(
            start=seg["start"] * 1000,
            end=seg["end"] * 1000,
            text=seg["text"]
        ))
    subs.save(output_path, format="srt")

def save_as_ass(subtitles, output_path, style=None):
    style = style or {}
    fontname = style.get("font", "Arial")
    fontsize = style.get("size", "48")
    primary_color = style.get("primary_color", "&H00FFFFFF")
    outline_color = style.get("outline_color", "&H00000000")
    outline = style.get("outline", "1")

    def _format_time(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = seconds % 60
        return f"{h:d}:{m:02d}:{s:05.2f}"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("[Script Info]\n")
        f.write("ScriptType: v4.00+\n")
        f.write("PlayResX: 1920\n")
        f.write("PlayResY: 1080\n")
        f.write("\n")

        f.write("[V4+ Styles]\n")
        f.write(
            f"Style: Default,{fontname},{fontsize},&H00FFFFFF,&H00FFFFFF,{primary_color},{outline_color},0,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1\n"
        )
        f.write("\n")

        f.write("[Events]\n")
        for segment in subtitles["segments"]:
            start = _format_time(segment["start"])
            end = _format_time(segment["end"])
            text = segment["text"].replace("\n", " ").replace(",", "，")
            f.write(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n")
