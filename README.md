<link href="https://cuongbokreal.github.io/face-detector-haarcascade/read-me/main.css" rel="stylesheet" />
face-detector-haarcascade - by CuongbokIT (https://cuongbokit.blogspot.com/)


<h4>Các bước thực hiện</h4>

<div data-message-author-role="assistant" data-message-id="1f55ced6-a382-4392-8758-3f89493dfb42" class="min-h-[20px] text-message flex flex-col items-start gap-3 whitespace-pre-wrap break-words [.text-message+&amp;]:mt-5 overflow-x-auto"><div class="markdown prose w-full break-words dark:prose-invert light"><p>Để sử dụng <code>haarcascade_frontalface_default.xml</code> để nhận diện khuôn mặt trong Python với OpenCV, bạn có thể tuân thủ các bước sau:</p><ol><li><p><strong>Cài đặt OpenCV:</strong>
Đảm bảo rằng bạn đã cài đặt thư viện OpenCV. Nếu chưa, sử dụng lệnh sau để cài đặt:</p>
<pre><div class="bg-black rounded-md">
<div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install opencv-python
</code></div></div></pre></li><li><p><strong>Import thư viện và tải Haar Cascade Classifier:</strong>
Import thư viện OpenCV và tải <code>haarcascade_frontalface_default.xml</code> từ thư viện mẫu của OpenCV:</p><pre><div class="bg-black rounded-md">
  
<div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> cv2

<span class="hljs-comment"># Tải Haar Cascade Classifier cho khuôn mặt</span>
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + <span class="hljs-string">'haarcascade_frontalface_default.xml'</span>)
</code></div></div></pre></li><li><p><strong>Đọc và xử lý ảnh hoặc video:</strong>
Bạn có thể sử dụng <code>cv2.VideoCapture()</code> để đọc video từ webcam hoặc tệp tin. Sau đó, sử dụng <code>detectMultiScale()</code> để phát hiện khuôn mặt trong các khung hình.</p>

<div>Truy cập code tại <a href="https://github.com/cuongbokreal/face-detector-haarcascade/blob/main/video-face-detect.py">/video-face-detect.py</a></div>

<p>Trong đoạn mã ở trên, <code>detectMultiScale()</code> sẽ trả về danh sách các khuôn mặt được phát hiện trong ảnh và sau đó, vẽ hình chữ nhật xung quanh chúng.</p></li><li><p><strong>Tinh chỉnh tham số:</strong>
Bạn có thể tinh chỉnh các tham số như <code>scaleFactor</code> và <code>minNeighbors</code> để điều chỉnh độ chính xác và hiệu suất của thuật toán. Thử nghiệm và điều chỉnh các giá trị này để phù hợp với nhu cầu của bạn.</p></li></ol><p>Lưu ý rằng ví dụ trên chỉ là một cách sử dụng cơ bản của Haar Cascade để nhận diện khuôn mặt. Bạn có thể tích hợp nó vào ứng dụng của mình và tùy chỉnh để đáp ứng yêu cầu cụ thể.</p></div></div>
