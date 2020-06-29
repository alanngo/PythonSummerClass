import cv2


def main():
    # create video object
    video = cv2.VideoCapture(0)

    # a variable
    a = 0

    while True:
        a = a + 1

        # create frame object
        check, frame = video.read()

        print(frame)
        print(check)

        # convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # show frame
        cv2.imshow("Capturing ", gray)

        # for press any key to out (milliseconds)
        # cv2.waitKey(0)

        # for playing
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

        print(a)

    # shut down camera
    video.release()
    cv2.destroyAllWindows()


main()
