import cv2

def scan_eyes():
    print("\n==============================")
    print("        OPEN YOUR EYES        ")
    print("==============================\n")
    print("Camera opening... Press Q to scan result.")

    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    cap = cv2.VideoCapture(0)

    detected_sizes = []

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        # Save eye sizes to analyze later
        for (x, y, w, h) in eyes:
            detected_sizes.append(w * h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

        cv2.imshow("Health Mirror - Eye Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # If no eyes detected at all
    if len(detected_sizes) == 0:
        print("\n❌ No eyes detected — Not normal. Take care of your eyes.\n")
        return

    # Average eye size
    avg_size = sum(detected_sizes) / len(detected_sizes)

    # Threshold for eye normal size (you can adjust)
    if avg_size > 800:
        print("\n✅ Normal — Your eyes look fine.\n")
    else:
        print("\n⚠ Not normal — Take care of your eyes.\n")


def main():
    print("==============================")
    print("      WELCOME TO HEALTH MIRROR")
    print("==============================")
    print("Press 1 to go to Health Mirror")

    choice = input("Enter: ")

    if choice == "1":
        scan_eyes()
    else:
        print("Invalid choice")


main()
