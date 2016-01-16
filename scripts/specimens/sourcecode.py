#!/usr/bin/env python
# -*- coding: utf-8 -*-

c_specimen="""
<span style="color: {{comment}}; font-style: italic">// sample code from commit.c of the Git repository (https://github.com/git)</span>

<span style="color: {{syntax}}">struct</span> <span style="color: {{syntax}}">commit</span> <span style="color: {{fg}}">*</span><span style="color: {{syntax}}">lookup_commit_or_die</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">const</span> <span style="color: {{constant}}; font-weight: bold">unsigned</span> <span style="color: {{constant}}; font-weight: bold">char</span> <span style="color: {{fg}}">*</span><span style="color: {{syntax}}">sha1</span><span style="color: {{fg}}">,</span> <span style="color: {{syntax}}">const</span> <span style="color: {{constant}}; font-weight: bold">char</span> <span style="color: {{fg}}">*</span><span style="color: {{syntax}}">ref_name</span><span style="color: {{fg}}">)</span>
<span style="color: {{fg}}">{</span>
    <span style="color: {{syntax}}">struct</span> <span style="color: {{syntax}}">commit</span> <span style="color: {{fg}}">*</span><span style="color: {{syntax}}">c</span> <span style="color: {{fg}}">=</span> <span style="color: {{syntax}}">lookup_commit_reference</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">sha1</span><span style="color: {{fg}}">);</span>
    <span style="color: {{syntax}}">if</span> <span style="color: {{fg}}">(!</span><span style="color: {{syntax}}">c</span><span style="color: {{fg}}">)</span>
        <span style="color: {{syntax}}">die</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">_</span><span style="color: {{fg}}">(</span><span style="color: {{content}}; font-weight: bold">&quot;could not parse %s&quot;</span><span style="color: {{fg}}">),</span> <span style="color: {{syntax}}">ref_name</span><span style="color: {{fg}}">);</span>
    <span style="color: {{syntax}}">if</span> <span style="color: {{fg}}">(</span><span style="color: {{syntax}}">hashcmp</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">sha1</span><span style="color: {{fg}}">,</span> <span style="color: {{syntax}}">c</span><span style="color: {{fg}}">-&gt;</span><span style="color: {{syntax}}">object</span><span style="color: {{fg}}">.</span><span style="color: {{syntax}}">sha1</span><span style="color: {{fg}}">))</span> <span style="color: {{fg}}">{</span>
        <span style="color: {{syntax}}">warning</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">_</span><span style="color: {{fg}}">(</span><span style="color: {{content}}; font-weight: bold">&quot;%s %s is not a commit!&quot;</span><span style="color: {{fg}}">),</span>
            <span style="color: {{syntax}}">ref_name</span><span style="color: {{fg}}">,</span> <span style="color: {{syntax}}">sha1_to_hex</span><span style="color: {{fg}}">(</span><span style="color: {{syntax}}">sha1</span><span style="color: {{fg}}">));</span>
    <span style="color: {{fg}}">}</span>
    <span style="color: {{syntax}}">return</span> <span style="color: {{syntax}}">c</span><span style="color: {{fg}}">;</span>
<span style="color: {{fg}}">}</span>
"""