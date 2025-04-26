# core/views.py

from django.shortcuts import render
import speedtest  # make sure you installed this package: pip install speedtest-cli

def speed_test(request):
    if request.method == 'POST':
        st = speedtest.Speedtest()
        download_speed = round(st.download() / (10**6), 2)  # convert to Mbps
        upload_speed = round(st.upload() / (10**6), 2)      # convert to Mbps
        ping = round(st.results.ping, 2)                    # in ms

        return render(request, 'index.html', {
            'download': download_speed,
            'upload': upload_speed,
            'ping': ping,
        })
    return render(request, 'index.html')
