import STT
import Translation
import SumModel

if __name__ == '__main__':
    str0 = STT.transcribe
    str1 = Translation.translation(str0)
    str2 = SumModel.run(str1)

    print(str2)
    with open("result.txt", "w") as f:
        f.write(str2)