#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use('agg')  # Use non-interactive backend for saving plots

import matplotlib.pyplot as plt
import numpy as np
import base64
import json

def prettyPicture(clf, X_test, y_test):
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    # Create mesh grid
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot decision boundary
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.seismic, shading='auto')

    # Plot test points
    grade_sig = [X_test[ii][0] for ii in range(len(X_test)) if y_test[ii] == 0]
    bumpy_sig = [X_test[ii][1] for ii in range(len(X_test)) if y_test[ii] == 0]
    grade_bkg = [X_test[ii][0] for ii in range(len(X_test)) if y_test[ii] == 1]
    bumpy_bkg = [X_test[ii][1] for ii in range(len(X_test)) if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")

    plt.savefig("test.png")


def output_image(name, format, bytes_data):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {
        'name': name,
        'format': format,
        'bytes': base64.b64encode(bytes_data).decode('utf-8')
    }
    print(image_start + json.dumps(data) + image_end)