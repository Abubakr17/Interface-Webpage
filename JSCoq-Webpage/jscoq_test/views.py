from django.shortcuts import render
import subprocess
import os

# Loads Main landing page of JSCoq
# If you get here after uploading an sml file
# then it loads the corresponding .v file 
# into JSCoq
def startPage(request):
    
    # No file has been uploaded
    if request.method == "GET":
        return render(request, 'index3.html')

    # Verify the existence of the uploaded file
    # and check that is an SML file
    if 'smlcode' in request.FILES:
        smlfile = request.FILES['smlcode']
        filename = str(request.FILES['smlcode'])
        if filename.endswith(".sml"):
            print("SML FILE Uploaded")
            
            # Save the file temporarily in local storage
            with smlfile.open() as smlf:
                tmp = open("jscoq_test/static/sml-to-coq/tmpsml.sml","wb")  ## obvious concurrency bug / fix later
                tmp.writelines(smlf.readlines())
                tmp.close()

            # Load the SML-to-Coq heap image to convert the SML file to a Coq file
            subprocess.run('cd jscoq_test/static/sml-to-coq && sml @SMLload sml2coq.amd64-darwin tmpsml.sml ../vfiles/tmp2.v', capture_output=True, shell=True)
            
            # Remove temp SML file
            if os.path.isfile('jscoq_test/static/sml-to-coq/tmpsml.sml'):
                os.remove('jscoq_test/static/sml-to-coq/tmpsml.sml')

            with open('jscoq_test/static/vfiles/tmp2.v') as vfile:
                txt = vfile.readlines()
            
            return render(request, 'index3.html', {'txt': txt})
    return render(request, 'index3.html')

def uploadPage(request):
    #print(subprocess.run('cd jscoq_test/static/sml-to-coq && sml @SMLload test-img.amd64-darwin induction.sml ../vfiles/pytest.v', capture_output=True, shell=True))
    return render(request, 'index.html')
    
def secondPage(request):
    return render(request, 'node_modules/jscoq/examples/equations_intro.html')