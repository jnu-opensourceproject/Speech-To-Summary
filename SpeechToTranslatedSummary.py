import Whisper

# import Translation



# import STT
# import Translation
from SummaryModule import SumModel
from opensource import translation


if __name__ == '__main__':
    whisperResult = Whisper.run()
    for wstr in whisperResult:
        str1 = translation.translate_to_korean(wstr["text"])
        print("Original: ", str1)
        str2 = SumModel.run(str1)
        print("Summary: ", str2, "\n")


    # with open("result.txt", "w") as f:
    #     f.write(str2)
