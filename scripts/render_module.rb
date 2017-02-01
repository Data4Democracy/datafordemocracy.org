# convert variable to liquid include tag
# use with coderunner
def render_module(name, locals)
  locals = locals[:locals]

  includes = []

  locals.each do |key, value|
    includes.push("#{key}='#{value}'")
  end

  if includes.empty?
    output = "{% include modules/#{name}.html %}"
  else
    output = "{% include modules/#{name}.html #{includes.join(' ')} %}"
  end

  puts output
end