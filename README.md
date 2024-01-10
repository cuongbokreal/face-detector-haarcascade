face-detector-haarcascade - by CuongbokIT (https://cuongbokit.blogspot.com/)


<h4>Các bước thực hiện</h4>

<div data-message-author-role="assistant" data-message-id="1f55ced6-a382-4392-8758-3f89493dfb42" class="min-h-[20px] text-message flex flex-col items-start gap-3 whitespace-pre-wrap break-words [.text-message+&amp;]:mt-5 overflow-x-auto"><div class="markdown prose w-full break-words dark:prose-invert light"><p>Để sử dụng <code>haarcascade_frontalface_default.xml</code> để nhận diện khuôn mặt trong Python với OpenCV, bạn có thể tuân thủ các bước sau:</p><ol><li><p><strong>Cài đặt OpenCV:</strong>
Đảm bảo rằng bạn đã cài đặt thư viện OpenCV. Nếu chưa, sử dụng lệnh sau để cài đặt:</p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install opencv-python
</code></div></div></pre></li><li><p><strong>Import thư viện và tải Haar Cascade Classifier:</strong>
Import thư viện OpenCV và tải <code>haarcascade_frontalface_default.xml</code> từ thư viện mẫu của OpenCV:</p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> cv2

<span class="hljs-comment"># Tải Haar Cascade Classifier cho khuôn mặt</span>
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + <span class="hljs-string">'haarcascade_frontalface_default.xml'</span>)
</code></div></div></pre></li><li><p><strong>Đọc và xử lý ảnh hoặc video:</strong>
Bạn có thể sử dụng <code>cv2.VideoCapture()</code> để đọc video từ webcam hoặc tệp tin. Sau đó, sử dụng <code>detectMultiScale()</code> để phát hiện khuôn mặt trong các khung hình.</p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-comment"># Đọc video từ webcam</span>
cap = cv2.VideoCapture(<span class="hljs-number">0</span>)

<span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:
    <span class="hljs-comment"># Đọc một khung hình từ video</span>
    ret, frame = cap.read()

    <span class="hljs-comment"># Chuyển đổi sang ảnh xám để tăng tốc độ xử lý</span>
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    <span class="hljs-comment"># Phát hiện khuôn mặt trong khung hình</span>
    faces = face_cascade.detectMultiScale(gray, scaleFactor=<span class="hljs-number">1.3</span>, minNeighbors=<span class="hljs-number">5</span>)

    <span class="hljs-comment"># Vẽ hình chữ nhật xung quanh khuôn mặt</span>
    <span class="hljs-keyword">for</span> (x, y, w, h) <span class="hljs-keyword">in</span> faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (<span class="hljs-number">255</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>), <span class="hljs-number">2</span>)

    <span class="hljs-comment"># Hiển thị kết quả</span>
    cv2.imshow(<span class="hljs-string">'Face Detection'</span>, frame)

    <span class="hljs-comment"># Thoát khỏi vòng lặp khi nhấn phím 'q'</span>
    <span class="hljs-keyword">if</span> cv2.waitKey(<span class="hljs-number">1</span>) &amp; <span class="hljs-number">0xFF</span> == <span class="hljs-built_in">ord</span>(<span class="hljs-string">'q'</span>):
        <span class="hljs-keyword">break</span>

<span class="hljs-comment"># Giải phóng tài nguyên</span>
cap.release()
cv2.destroyAllWindows()
</code></div></div></pre><p>Trong đoạn mã trên, <code>detectMultiScale()</code> sẽ trả về danh sách các khuôn mặt được phát hiện trong ảnh và sau đó, vẽ hình chữ nhật xung quanh chúng.</p></li><li><p><strong>Tinh chỉnh tham số:</strong>
Bạn có thể tinh chỉnh các tham số như <code>scaleFactor</code> và <code>minNeighbors</code> để điều chỉnh độ chính xác và hiệu suất của thuật toán. Thử nghiệm và điều chỉnh các giá trị này để phù hợp với nhu cầu của bạn.</p></li></ol><p>Lưu ý rằng ví dụ trên chỉ là một cách sử dụng cơ bản của Haar Cascade để nhận diện khuôn mặt. Bạn có thể tích hợp nó vào ứng dụng của mình và tùy chỉnh để đáp ứng yêu cầu cụ thể.</p></div></div>
